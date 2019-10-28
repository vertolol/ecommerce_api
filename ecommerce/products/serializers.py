from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'link',
            'slug',
            'category',
            'attributes',
            )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
