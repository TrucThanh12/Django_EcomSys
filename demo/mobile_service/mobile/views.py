from debugpy.common.messaging import Response
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Brand, Mobile
from .serializer import BrandSerializer, MobileSerializer, MobileInfoSerializer, UpdateMobileSerializer


class CreateBrandView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.filter(is_active__in=[True]).all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteBrandView(APIView):
    def delete(self, request, brand_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                brand = Brand.objects.get(brand_id=brand_id)
            except Brand.DoesNotExist:
                return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = BrandSerializer()
            serializer.destroy(author)

            return Response({'message': 'Brand soft deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateMobileView(APIView):
    def post(self, request):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            serializer = MobileSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class MobileListView(APIView):
    def get(self,request):
        mobiles = Mobile.objects.filter(is_active__in=[True]).all()
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MobileListOfBrandView(APIView):
    def get(self,request,brand_id):
        mobiles = Mobile.objects.filter(brand_id=brand_id,is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SearchMobileListView(APIView):
    def get(self,request,key):
        mobiles = Mobile.objects.filter(title__icontains=key,is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MobileDetailView(APIView):
    def get(self,request,mobile_id):
        mobiles = Mobile.objects.filter(mobile_id=mobile_id,is_active__in=[True]).first()
        serializer = MobileInfoSerializer(mobiles)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateMobileView(APIView):
    def put(self,request,mobile_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(mobile_id=mobile_id)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateMobileSerializer(mobile,data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalis token.'}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteMobileView(APIView):
    def delete(self,request,mobile_id):
        token_verification_url = "http://127.0.0.1:4000/api/ecomSys/user/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(mobile_id=mobile_id)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = MobileSerializer()
            serializer.destroy(mobile)

            return Response({'message': 'Mobile soft deleted'},status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
