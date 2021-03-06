# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

import json


class NumpyFunction(models.Model):
    """
    Class for running numpy functions on lambda
        numpy_source - Source code of function
        json - output
    """
    title = models.CharField(max_length=2**8)
    numpy_source = models.TextField(blank=True)
    json = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def numpy_func_fn(self):
        """
        Strip space from title for filename to output function to
        """
        return ''.join(self.title.split())


class NumpyDataStructure(models.Model):
    numpy_function = models.ForeignKey(NumpyFunction, on_delete=models.CASCADE, related_name='data')
    csv = models.FileField(upload_to='csvs/')
    key = models.CharField(max_length=2*7)


@receiver(post_save, sender=NumpyFunction)
def _write_func(sender, instance, created, **kwargs):
    """
        Write function to file, run with provided csvs as kwargs. 
        Save json output in field. 
    """
    if (instance.numpy_source and instance.numpydatastructure_set.exists()):
        func_dict = {}
        ds_out = [func_dict.update({dat.key:dat.csv.file}) for dat in instance.numpydatastructure_set.all()]
        fp = open('{}.py'.format(instance.numpy_func_fn),'w')
        fp.write(instance.numpy_source)
        fp.close()
        np_func = __import__(instance.numpy_func_fn)
        returned_json_data = json.loads(np_func.main(**func_dict))
        sender.objects.filter(id=instance.id).update(json=returned_json_data)
