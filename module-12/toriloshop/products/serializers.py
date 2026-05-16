from rest_framework import serializers  # pyright: ignore[reportMissingModuleSource]
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        # ' __all __ ' includes every field on the model
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()

class ProductSerializer(serializers.ModelSerializer):
     # Nested serializer - shows full category object instead of just the ID
     # read_only=True means this field is output only - not used for input
    category = CategorySerializer(read_only=True)

      # category_id accepts a category ID when creating/updating a product
     # write_only=True means it is only used for input - not shown in output
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'is_available', 'created_at', 'category', 'category_id']

