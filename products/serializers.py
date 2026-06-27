from rest_framework import serializers
from .models import Producto


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = "__all__"

class DesactivateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["status"]
        read_only_fields = ["status"]

    def update(self, instance, validated_data):
        instance.status = False
        instance.save()
        return instance
