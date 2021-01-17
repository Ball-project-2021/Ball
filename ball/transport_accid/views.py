from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TransportAccidModel
from .serializers import TransportAccidDetailSerializer, TransportAccidListSerializer

# class TransportsView(ListAPIView):
#     serializer_class = TransportSerializer
#     queryset = TransportFieldsModel.objects.all()


class TransportAccidListView(APIView):

    def get(self, request):
        trasports = TransportAccidModel.objects.all()
        serializer = TransportAccidListSerializer(trasports, many=True)
        return Response(serializer.data)


class TransportAccidDetailView(APIView):

    def get(self, request, pk):
        trasport = TransportAccidModel.objects.get(id=pk)
        serializer = TransportAccidDetailSerializer(trasport)
        return Response(serializer.data)