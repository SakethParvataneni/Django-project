# api/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer

@api_view(['POST'])
def ingest_url(request):
    serializer = URLSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_urls(request):
    spidername = request.query_params.get('spidername')
    if spidername:
        urls = URL.objects.filter(spidername=spidername, status='pending').order_by('-priority')
    else:
        urls = URL.objects.filter(status='pending').order_by('-priority')
    serializer = URLSerializer(urls, many=True)
    return Response(serializer.data)
