from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CategorySerializer
from .models import Category


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
