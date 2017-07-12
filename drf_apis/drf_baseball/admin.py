# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NumpyFunction, NumpyDataStructure

class NumpyDataStructureInline(admin.TabularInline):
    model = NumpyDataStructure

class NumpyFunctionAdmin(admin.ModelAdmin):
    inlines = [
        NumpyDataStructureInline,
    ]

admin.site.register(NumpyFunction, NumpyFunctionAdmin)
