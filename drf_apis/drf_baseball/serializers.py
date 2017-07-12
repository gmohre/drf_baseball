from rest_framework import serializers
from .models import NumpyFunction, NumpyDataStructure

class NumpyFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyFunction
        fields = ('__all__')

class NumpyDataStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyDataStructure
        fields = ('__all__')
