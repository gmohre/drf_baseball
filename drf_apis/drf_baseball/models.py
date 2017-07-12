# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

class NumpyFunction(models.Model):
    title = models.CharField(max_length=2**8)
    numpy_source = models.TextField()
    json = models.TextField()

    """
    Stored file could be zip file or csv.
    """
    #STORE ON S3 csv_input = models.FileField()

    def __str__(self):
        return self.title

    @property
    def numpy_func_fn(self):
        return ''.join(self.title.split())

    def write_func(self):
        func_dict = {}
        ds_out = [func_dict.update({dat.key:dat.csv.file}) for dat in self.numpydatastructure_set.all()]
        try:
            open('{}.py'.format(self.numpy_func_fn),'w').write(self.numpy_source)
        except:
            print('bust')
        np_func = __import__(self.numpy_func_fn)
        self.json = json.loads(np_func.main(**func_dict))
        self.save()


class NumpyDataStructure(models.Model):
    numpy_function = models.ForeignKey(NumpyFunction, on_delete=models.CASCADE)
    csv = models.FileField(upload_to='csvs/')
    key = models.CharField(max_length=2*7)
# Create your models here.w
