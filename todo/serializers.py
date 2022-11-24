# todo/serializers.py

from rest_framework import serializers
from .models import TodoList, Category

class CategorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Category
            fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
      class Meta:
            model = TodoList
            fields = "__all__"