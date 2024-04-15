from django.contrib import admin
from django.urls import path
from .views import RegisterView,LoginView,UserInfoView,ChangePasswordView,UpdateProfileView,VerifyTokenView

urlpatterns = [
    path('api/ecomSys/user/register/', RegisterView.as_view(), name='register'),
    path('api/ecomSys/user/login/', LoginView.as_view(), name='login'),
    path('api/ecomSys/user/info/',UserInfoView.as_view(), name='info'),
    path('api/ecomSys/user/change/',ChangePasswordView.as_view(), name='change'),
    path('api/ecomSys/user/update/',UpdateProfileView.as_view(), name='update'),
    path('api/ecomSys/user/verify-token/',VerifyTokenView.as_view(), name='verify-token')
]
