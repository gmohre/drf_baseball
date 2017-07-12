from rest_framework import serializers
from .models import NumpyFunction, NumpyDataStructure

class NumpyDataStructureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NumpyDataStructure
        fields = ('__all__')

class NumpyFunctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = NumpyFunction
        fields = ('title', 'numpy_source', 'json', 'data')
        depth = 1


