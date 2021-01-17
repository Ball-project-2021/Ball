# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .serializers import TransportSerializer
# from .models import TransportFieldsModel
# from rest_framework.parsers import JSONParser
# from rest_framework.generics import ListAPIView, RetrieveAPIView
#

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wheel
from .serializers import WheelListSerializer, WheelDetailSerializer

# class TransportsView(ListAPIView):
#     serializer_class = TransportSerializer
#     queryset = TransportFieldsModel.objects.all()


class WheelListView(APIView):

    def get(self, request):
        wheels = Wheel.objects.all()
        serializer = WheelListSerializer(wheels, many=True)
        return Response(serializer.data)


class WheelDetailView(APIView):

    def get(self, request, pk):
        wheel = Wheel.objects.get(id=pk)
        serializer = WheelDetailSerializer(wheel)
        return Response(serializer.data)