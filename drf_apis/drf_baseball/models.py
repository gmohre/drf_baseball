# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
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
        return ''.join(self.title.split())

    def save(self, *args, **kwargs):
        super(NumpyFunction, self).save(*args, **kwargs)
        self._write_func()

    def _write_func(self):
        """
            Write function to file, run with provided csvs as kwargs. 
            Save json output in field. 
        """
        if self.numpy_source and self.numpydatastructure_set.count():
            func_dict = {}
            ds_out = [func_dict.update({dat.key:dat.csv.file}) for dat in self.numpydatastructure_set.all()]
            try:
                open('{}.py'.format(self.numpy_func_fn),'w').write(self.numpy_source)
            except:
                print('bust')
            np_func = __import__(self.numpy_func_fn)
            self.json = json.loads(np_func.main(**func_dict))
            self.save(update_fields=['json'])



class NumpyDataStructure(models.Model):
    numpy_function = models.ForeignKey(NumpyFunction, on_delete=models.CASCADE)
    csv = models.FileField(upload_to='csvs/')
    key = models.CharField(max_length=2*7)
