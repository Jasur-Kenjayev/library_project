from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerialzer
from rest_framework import generics, status
from .models import Book

# class BookListApiWiew(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialzer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerialzer(books, many=True).data
        data = {
            "status": f'Returned {len(books)} books',
            "books": serializer_data
        }

        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialzer

class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerialzer(book).data

            data = {
                "ststus": "Seccussfull",
                "book": serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"ststus": "False",
                 "message": "Book is not found"}, status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialzer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book =  Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Successfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "message": "Book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialzer

class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerialzer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
            "status": True,
            "message": f"Book {book_saved} updated successfully"
            }
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialzer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerialzer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {'status': f'Books are saved to the database',
                    'books': data
                    }
            return Response(data)

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
