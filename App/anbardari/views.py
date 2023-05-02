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

        return Response({"data1": serializer1.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer2=NouSerializers(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

        return Response({"errorsq2":serializer2.errors,"errorsq":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
