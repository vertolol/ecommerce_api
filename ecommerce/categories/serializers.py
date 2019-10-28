from rest_framework import serializers
from .models import Category
from products.serializers import ProductSerializer


import re
from django.db.models import Q


FILTER_PRICE = 'price'
FILTER_RANGE = 'fr'
FILTER_CONTAINS = 'f'


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, category):
        parameters = self.context['request'].query_params
        queryset = category.product.all()

        if parameters:
            queryset = self.query_filtering(queryset, parameters)

        data_products = ProductSerializer(instance=queryset, many=True).data
        count_products = queryset.count()

        return {'total': count_products, 'info': data_products}

    @staticmethod
    def query_filtering(queryset, parameters):
        filter_range = dict()
        filter_contains = Q()

        for name in parameters:
            if name == FILTER_PRICE:
                filter_value = parameters[name].split('-')
                low, high = map(float, filter_value)
                filter_range[f'price__range'] = (low, high)
                continue

            filter_detail = re.search(r'(\w*)\[(\w*)\]', name)
            filter_type = filter_detail.group(1)
            filter_name = filter_detail.group(2)
            filter_value = parameters[name].split('-')

            if filter_type == FILTER_CONTAINS:
                contains = Q()
                for value in filter_value:
                    contains.add(Q(attributes__contains={filter_name: value}), Q.OR)
                filter_contains.add(contains, Q.AND)

            elif filter_type == FILTER_RANGE:
                low, high = map(float, filter_value)
                filter_range[f'attributes__{filter_name}__gte'] = low
                filter_range[f'attributes__{filter_name}__lt'] = high

        return queryset.filter(filter_contains, **filter_range)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent_link',
            'level',
            'children_node_info',
            'products',
            'attributes'
            )
