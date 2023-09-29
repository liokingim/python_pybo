from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!!!')

@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello World drf!!'})