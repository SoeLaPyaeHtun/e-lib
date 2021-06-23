from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Book, Author, Category
from .serializers import BookModelSerializer, AuthorModelSerializer, CategoryModelSerializer


class BookModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class AuthorModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class CategoryModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
