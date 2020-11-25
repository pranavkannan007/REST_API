#pylint: disable=unused-argument
# pylint: disable=unused-variable
# pylint: enable=too-many-lines

from RESTAPIinsert.models import Booksmodel
from RESTAPIinsert.serialize import Bookserialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests

@api_view(['POST'])
def savebook(request):
    if request.method=="POST":
        saveserialize=Bookserialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data,status=status.HTTP_201_CREATED)
            return Response(saveserialize.data,status=status.HTTP_400_BAD_REQUEST)

def insertbook(request):
    if request.method=="POST":
        BookName=request.POST.get('BookName')
        Author=request.POST.get('Author')
        Genre=request.POST.get('Genre')
        PublishedYear=request.POST.get('PublishedYear')
        data={'BookName':BookName,'Author':Author,'Genre':Genre,'PublishedYear':PublishedYear}
        headers={'Content-Type':'application/json'}
        read=requests.post('http://127.0.0.1:8000/insertbookapi',json=data,headers=headers)
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')
