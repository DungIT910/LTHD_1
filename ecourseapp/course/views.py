from rest_framework import viewsets, generics
from .models import Category, Course
from . import serializers


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
