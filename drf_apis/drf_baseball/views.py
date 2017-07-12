# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import NumpyFunction
from .serializers import NumpyFunctionSerializer


class NumpyFunctionViewSet(viewsets.ModelViewSet):
    queryset = NumpyFunction.objects.all()
    serializer_class = NumpyFunctionSerializer
