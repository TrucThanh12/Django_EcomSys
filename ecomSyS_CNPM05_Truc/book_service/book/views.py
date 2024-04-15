from debugpy.common.messaging import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Category, Author, Publisher, Book
from .serializers import CategorySerializer, AuthorSerializer, PublisherSerializer, BookSerializer, BookInfoSerializer, UpdateBookSerializer


# Them category ( cần gọi server de xac thuc)
class CreateCategoryView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


# Hien thi tat ca category
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(is_active__in=[True]).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Them author  ( cần gọi server de xac thuc)
class CreateAuthorView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            serializer = AuthorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


# Them publisher  ( cần gọi server de xac thuc)
class CreatePublisherView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            serializer = PublisherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


# Xóa Category  ( cần gọi server de xac thuc)
class DeleteCategoryView(APIView):
    def delete(self, request, category_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                category = Category.objects.get(category_id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CategorySerializer()
            serializer.destroy(category)

            return Response({'message': 'Category soft deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


# Xóa author  ( cần gọi server de xac thuc)
class DeleteAuthorView(APIView):
    def delete(self, request, author_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                author = Author.objects.get(author_id=author_id)
            except Author.DoesNotExist:
                return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = AuthorSerializer()
            serializer.destroy(author)

            return Response({'message': 'Author soft deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

# Xóa publisher  ( cần gọi server de xac thuc)
class DeletePublisherView(APIView):
    def delete(self, request, publisher_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                publisher = Publisher.objects.get(publisher_id=publisher_id)
            except Publisher.DoesNotExist:
                return Response({'error': 'Publisher not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = PublisherSerializer()
            serializer.destroy(publisher)

            return Response({'message': 'Publisher soft deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

# Them book  ( cần gọi server de xac thuc)
class AddBookView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        print(headers)
        response = requests.get(token_verification_url, headers=headers)
        print(response)
        if response.status_code == 200:
            serializer = BookSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status = status.HTTP_401_UNAUTHORIZED)

# Hien thi tat ca book
class BookListView(APIView):
    def get(self,request):
        books = Book.objects.filter(is_active__in=[True]).all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Loc book theo category
class BookListOfCategoryView(APIView):
    def get(self,request,category_id):
        books = Book.objects.filter(category_id=category_id, is_active__in=[True])
        serializer = BookInfoSerializer(books, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Tim kiem book bang keywork
class SearchBookListView(APIView):
    def get(self, request, key):
        books = Book.objects.filter(Q(title__icontains=key)|Q(author__icontains=key), is_active__in=[True])
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Xem thong tin detail book
class BookDetailView(APIView):
    def get(self,request, book_id):
        book = Book.objects.filter(id=book_id, is_active__in=[True]).first()
        serializer = BookInfoSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Cap nhat thong tin book  ( cần gọi server de xac thuc)
class UpdateBookView(APIView):
    def put(self, request, book_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                book = Book.objects.get(book_id=book_id)
            except:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = UpdateBookSerializer(book)
            serializer.destroy(book)

            return Response({'message': 'Book sofr deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

# Xoa book  ( cần gọi server de xac thuc)
class DeleteBookView(APIView):
    def delete(self, request, book_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                book = Book.objects.get(book_id=book_id)
            except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer()
            serializer.destroy(book)

            return Response({'message': 'Book soft deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
