from django.shortcuts import render
from stocks.models import plants, order
from stocks.serializers import PlantSerializers, OrderSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.permissions import ClientPermission, AdminPermission

# Create your views here.
class PlantsListCreateAPIView(ListCreateAPIView):
    serializer_class = PlantSerializers
    queryset = plants.objects.all()
    # permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        serializer.save(supplier=self.request.user)
        
class PlantsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializers
    queryset = plants.objects.all()
    # permission_classes = [AdminPermission]

    # def perform_create(self, serializer):
    #     serializer.save(supplier=self.request.user)    

class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializers
    queryset = order.objects.all()
    permission_classes = [AdminPermission | ClientPermission]

class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializers
    queryset = order.objects.all()
    permission_classes = [AdminPermission | ClientPermission]
