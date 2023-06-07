from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import FruitStore
from .serializers import FruitStoreSerializer


class FruitStoreCreateView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = FruitStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) #http status : 200, 201 -> success
        return Response(serializer.errors, status=400)  #http status :4xx, 5xx -> fail

class FruitStoreListView(APIView):
    @csrf_exempt
    def get(self, request):
        users = FruitStore.objects.all()
        serializer = FruitStoreSerializer(users, many=True)
        return Response(serializer.data)

class FruitStoreDetailView(APIView):
    @csrf_exempt
    def get(self, request, pk):
        user = FruitStore.objects.get(pk=pk)

        serializer = FruitStoreSerializer(user)
        return Response(serializer.data)

class FruitStoreUpdateView(APIView):
    @csrf_exempt
    def put(self, request, pk):
        fruitstore = FruitStore.objects.get(pk=pk)

        serializer = FruitStoreSerializer(fruitstore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class FruitStoreDeleteView(APIView):
    @csrf_exempt
    def delete(self, request, pk):
        fruitstore = FruitStore.objects.get(pk=pk)

        fruitstore.delete()
        return Response(status=204)
