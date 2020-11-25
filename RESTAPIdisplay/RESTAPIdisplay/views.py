from RESTAPIdisplay.serialization import Serializationclass
from RESTAPIdisplay.models import Booksmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests

@api_view(['GET'])
def showbook(request):
    if request.method=='GET':
        results=Booksmodel.objects.all()
        serialize=Serializationclass(results,many=True)
        return Response(serialize.data)

def displaydata(request):
    callapi=requests.get('http://127.0.0.1:8000/Show')
    results=callapi.json()
    return render(request,'index.html',{'Booksmodel':results})