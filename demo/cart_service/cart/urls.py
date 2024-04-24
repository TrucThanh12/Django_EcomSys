from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import AddToCartView,CartView, DeleteCartItemView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecomSys/cart/add/',AddToCartView.as_view()),
    path('api/ecomSys/cart/show/',CartView.as_view()),
    path('api/ecomSys/cart/delete/<str:product_id>/', DeleteCartItemView.as_view())

]