from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


def get_total(instance):
    total = sum([product.price for product in instance.products.all()])


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product', 'total']