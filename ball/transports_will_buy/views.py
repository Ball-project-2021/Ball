from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TransportFieldsModel
from .serializers import TransportWillBuyDetailSerializer, TransportWillBuyListSerializer

# class TransportsView(ListAPIView):
#     serializer_class = TransportSerializer
#     queryset = TransportFieldsModel.objects.all()


class TransportWillBuyListView(APIView):

    def get(self, request):
        trasports = TransportFieldsModel.objects.all()
        serializer = TransportWillBuyListSerializer(trasports, many=True)
        return Response(serializer.data)


class TransportWillBuyDetailView(APIView):

    def get(self, request, pk):
        trasport = TransportFieldsModel.objects.get(id=pk)
        serializer = TransportWillBuyDetailSerializer(trasport)
        return Response(serializer.data)