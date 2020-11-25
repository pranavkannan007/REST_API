from rest_framework import serializers
from RESTAPIinsert.models import Booksmodel

class Bookserialize(serializers.ModelSerializer):
    class Meta:
        model=Booksmodel
        fields="__all__"