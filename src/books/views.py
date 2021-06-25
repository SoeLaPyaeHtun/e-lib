from django.shortcuts import render
from rest_framework import response, serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Book, Author, Category
from .serializers import BookModelSerializer
from rest_framework.decorators import api_view
# class BookModelAPIViewSet(viewsets.ModelViewSet):
#     serializer_class = BookModelSerializer
#     queryset = Book.objects.all()


# class AuthorModelAPIViewSet(viewsets.ModelViewSet):
#     serializer_class = AuthorModelSerializer
#     queryset = Author.objects.all()


# class CategoryModelAPIViewSet(viewsets.ModelViewSet):
#     serializer_class = CategoryModelSerializer
#     queryset = Category.objects.all()


# @api_view(['GET'])
# def BookModelAPIViewSet(request):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer(queryset)
#     return response(serializer_class.data)


@api_view(['GET'])
def Book_Get(request):
    tasks = Book.objects.all()
    serializers = BookModelSerializer(tasks, many=True)
    return Response(serializers.data)
