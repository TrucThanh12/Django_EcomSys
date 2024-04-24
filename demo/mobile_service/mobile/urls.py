from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CreateBrandView, CreateMobileView, BrandListView, MobileListView, MobileDetailView, \
    MobileListOfBrandView, SearchMobileListView, UpdateMobileView, DeleteBrandView, DeleteMobileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecomSys/brand/add/', CreateBrandView.as_view()),
    path('api/ecomSys/brand/all/', BrandListView.as_view()),
    path('api/ecomSys/brand/delete/<str:brand_id>/', DeleteBrandView.as_view()),
    path('api/ecomSys/mobile/add/', CreateMobileView.as_view()),
    path('api/ecomSys/mobile/all/', MobileListView.as_view()),
    path('api/ecomSys/mobile/detail/<str:mobile_id>/',MobileDetailView.as_view()),
    path('api/ecomSys/mobile/brand/<str:brand_id>/', MobileListOfBrandView.as_view()),
    path('api/ecomSys/mobile/search/<str:key>', SearchMobileListView.as_view()),
    path('api/ecomSys/mobile/update/<str:mobile_id>/', UpdateMobileView.as_view()),
    path('api/ecomSys/mobile/delete/<str:mobile_id>/', DeleteMobileView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
