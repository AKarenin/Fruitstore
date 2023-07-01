from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import FruitStore
from .serializers import FruitStoreSerializer, FruitMenuSerializer


# client(ui) -> server(data management)
# 아래 일을 왜 서버한테 시켜야할까요? (서버는 24시간 켜져잇기 때문애)
# (봇)특정 데이터를 감시하시면서, 변경이 일어났거나, 특정 조건에서, 무슨 처리를 해줘.

# 보통의상황
# 클라이언트(ui, flutter)에서 데이터 저장소를 뭘 쓰고 있을까요? 서버 저장소.(db.sqlite3)
# 서버는 데이터 저장소를 뭘 쓰고 있을까요? 서버 저장소 (db.sqlite3)

# 현상황
# 클라이언트(ui, flutter)에서 데이터 저장소를 뭘 쓰고 있을까요? firestore
# 서버는 데이터 저장소를 뭘 쓰고 있을까요? 서버 저장소, firestore 연동


class FruitStoreCreateView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = FruitStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # http status : 200, 201 -> success
        return Response(serializer.errors, status=400)  # http status :4xx, 5xx -> fail


class FruitStoreListView(APIView):
    @csrf_exempt
    def get(self, request):
        fruitStores = FruitStore.objects.all()  # 여기에 프루트메뉴즈가 있는데, 여기는 변환된프루트스토어가 없다.
        fruitStoreSerializer = FruitStoreSerializer(fruitStores, many=True)
        fruitStoreList = fruitStoreSerializer.data

        return Response({
            'fruitStoreList': fruitStoreList,
        })


class FruitStoreDetailView(APIView):
    @csrf_exempt
    def get(self, request, pk):
        user = FruitStore.objects.get(pk=pk)

        serializer = FruitStoreSerializer(user)
        return Response(serializer.data)


class FruitStoreFilterByLoc(APIView):
    @csrf_exempt
    def get(self, request, location):
        fruitstores = FruitStore.objects.filter(location=location)
        serializer = FruitStoreSerializer(fruitstores, many=True)
        return Response(serializer.data)


class FruitStoreFilterByName(APIView):
    @csrf_exempt
    def get(self, request, namepart):
        try:
            fruitstores = FruitStore.objects.filter(name__icontains=namepart)
            serializer = FruitStoreSerializer(fruitstores, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=400)


# crud. create, read, update, delete
# post(create), put(update), delete(delete), get(read)
class FruitStoreFindPnView(APIView):
    @csrf_exempt
    def get(self, request, phoneNumber):
        try:
            fruitstore = FruitStore.objects.get(phoneNumber=phoneNumber)
            serializer = FruitStoreSerializer(fruitstore)
            return Response(serializer.data)
        except:
            return Response('no match', status=400)


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
