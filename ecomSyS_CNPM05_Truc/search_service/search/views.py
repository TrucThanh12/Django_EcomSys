from django.views.generic import TemplateView
from debugpy.common.messaging import Response
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Search
from .serializers import SearchSerializer


class SearchView(APIView):
    def post(self,request):
        key = request.query_params.get('key','')
        token_verification_url = "https://127.0.0.1:4000/api/ecomSys/user/info/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = request.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            user_id = response.json().get('id')
            Search.objects.create(key=key,user_id=user_id)

        result = []
        result += self.search_book(key)
        result += self.search_mobile(key)

        return Response(data=result, status=status.HTTP_200_OK)
    def search_book(self,key):
        book_service_url = "https://127.0.0.1:4002/api/ecomSys/book/search/{}/".format(key)
        book_response = requests.get(book_service_url)
        if book_response.status_code == 200:
            return book_response.json()
        return []

    def search_mobile(self,key):
        mobile_service_url = "https://127.0.0.1:4005/api/ecomSys/mobile/search/{}/".format(key)
        mobile_response = requests.get(mobile_service_url)
        if mobile_response.status_code == 200:
            return mobile_response.json()
        return []

    def search_clothes(self,key):
        clothes_service_url = "https://127.0.0.1:4006/api/ecomSys/clothes/search/{}/".format(key)
        clothes_response = requests.get(clothes_service_url)
        if clothes_response.status_code == 200:
            return clothes_response.json()
        return []

# hien thi thong tin search cuar user
class ShowSearchView(APIView):
    def get(self,request):
        token_verification_url = "https://127.0.0.1:4000/api/ecomSys/user/info/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            user_id = response.json().get('id')
            searchs_instance = Search.objects.filter(is_active=True, user_id=user_id).all()
            serializer = SearchSerializer(searchs_instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

# xoa thong tin search cuar nguoi dung
class DeleteSearchView(APIView):
    def delete(self,request,key):
        token_verification_url = "https://127.0.0.1:4000/api/ecomSys/user/info/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            user_id = response.json().get('id')
            try:
                search = Search.objects.get(user_id=user_id, key=key, is_active=True)
            except:
                return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)

            serializer = SearchSerializer()
            serializer.destroy(search)

            return Response({'message': 'Search soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
