from rest_framework import serializers

from product.models import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        source="categories",
        queryset=Category.objects.all(),
        write_only=True,
        many=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "categories",
            "categories_id",
        ]

    def create(self, validated_data):
        categories = validated_data.pop("categories", [])
        product: Product = Product.objects.create(**validated_data)
        product.categories.set(categories)

        return product