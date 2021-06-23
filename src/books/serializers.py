from django.db import models
from rest_framework import serializers
from .models import Book, Author, Category


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
