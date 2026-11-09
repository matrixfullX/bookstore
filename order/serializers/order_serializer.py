from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True,
    )
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["product", "product_id", "total", "user"]

    @staticmethod
    def get_total(instance):
        return sum(item.price or 0 for item in instance.product.all())

    def create(self, validated_data):
        products = validated_data.pop("product_id")
        order: Order = Order.objects.create(**validated_data)
        order.product.set(products)
        return order