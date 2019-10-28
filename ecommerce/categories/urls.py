from django.urls import path
from .views import CategoryView, SingleCategoryView


urlpatterns = [
    path('', CategoryView.as_view()),
    path('<str:slug>/', SingleCategoryView.as_view(), name='category_detail')
]
