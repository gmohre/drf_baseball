# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class NumpyFunction(models.Model):
    title = models.CharField(max_length=2**8)
    numpy_source = models.TextField()
    json = models.TextField()

    """
    Stored file could be zip file or csv.
    """
    #STORE ON S3 csv_input = models.FileField()

    def __str__(self):
        return "{} - {}".format(self.title, self.numpy_source)
# Create your models here.w
