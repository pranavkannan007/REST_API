from rest_framework import serializers
from RESTAPIdisplay.models import Booksmodel

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Booksmodel
        fields='__all__'