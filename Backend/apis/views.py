# apis/views.py
from rest_framework import generics

from library_app.models import Books
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer


@api_view(['GET'])
def getData(request):
    all_books = Books.objects.all()
    all_books = BookSerializer(all_books, many=True)
    return Response(all_books.data)


@api_view(['POST'])
def loadData(request):
    new_book = BookSerializer(data=request.data)
    if new_book.is_valid():
        new_book.save()
    return Response(new_book.data)


