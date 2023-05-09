from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import *


class shop(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # print(request.GET["id"])
        # queriset1 = Nou.objects.all()
        # serializer1 = NouSerializers(queriset1, many=True)

        queriset = Product.objects.all()
        serializer = ProductSerializers(queriset, many=True)

        return Response({"data1": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer2 = NouSerializers(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

        return Response({"errorsq2": serializer2.errors, "errorsq": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        product = Product.objects.get(pk=data['id'])
        nou = Nou.objects.get(pk=data['nouid'])
        product.nou = nou
        product.count = data['count']
        product.submitdate = data['submitdate']
        product.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.DELETE
        product = Product.objects.get(pk=data['id'])
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
