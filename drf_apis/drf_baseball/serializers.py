from rest_framework import serializers
from .models import NumpyFunction

class NumpyFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyFunction
        fields = ('__all__')
