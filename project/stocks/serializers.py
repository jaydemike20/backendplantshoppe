from rest_framework import serializers
from stocks.models import plants, order
from accounts.serializers import CustomUserSerializer


class PlantSerializers(serializers.ModelSerializer):
    supplier = CustomUserSerializer(read_only=True)

    class Meta:
        model = plants
        fields = "__all__"
        read_only_fields = ('supplier',)  # It should be a tuple


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = "__all__"