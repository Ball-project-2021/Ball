from django.shortcuts import render
from .serializers import TransportSerializer
from .models import TransportFieldsModel
from rest_framework.generics import ListAPIView, RetrieveAPIView


class TransportsView(ListAPIView):
    serializer_class = TransportSerializer
    queryset = TransportFieldsModel.objects.all()

    print(queryset)



