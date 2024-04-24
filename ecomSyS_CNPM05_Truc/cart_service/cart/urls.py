from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import AddToCartView,CartView, DeleteCartItemView
urlpatterns = [
    path('add/',AddToCartView.as_view()),
    path('show/',CartView.as_view()),
    path('delete/<str:product_id>/', DeleteCartItemView.as_view())
]