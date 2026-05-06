from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from .models import Client
from .serializers import ClientSerializer



import json


@api_view(['GET'])
def list_clients(request):
    if request.method == "GET":
        clients = Client.objects.all()         
        serializer = ClientSerializer(clients,many = True)  
    
        return Response(serializer.data)


@api_view(['POST'])
def save_client(request):
  
    serializer = ClientSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_client(requesi,id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return Response(status.HTTP_204_NO_CONTENT )

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')