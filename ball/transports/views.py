# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .serializers import TransportSerializer
# from .models import TransportFieldsModel
# from rest_framework.parsers import JSONParser
# from rest_framework.generics import ListAPIView, RetrieveAPIView
#

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TransportFieldsModel
from .serializers import TransportListSerializer, TransportDetailSerializer

# class TransportsView(ListAPIView):
#     serializer_class = TransportSerializer
#     queryset = TransportFieldsModel.objects.all()


class TransportListView(APIView):

    def get(self, request):
        trasports = TransportFieldsModel.objects.all()
        serializer = TransportListSerializer(trasports, many=True)
        return Response(serializer.data)


class TransportDetailView(APIView):

    def get(self, request, pk):
        trasport = TransportFieldsModel.objects.get(id=pk)
        serializer = TransportDetailSerializer(trasport)
        return Response(serializer.data)