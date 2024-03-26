from rest_framework import serializers
from .models import Category, BaseModel, Course


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'
