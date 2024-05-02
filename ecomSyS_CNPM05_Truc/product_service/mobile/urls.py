from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CreateBrandView, CreateMobileView, BrandListView, MobileListOfBrandView, MobileListView, \
    DeleteBrandView, UpdateMobileView, DeleteMobileView, MobileDetailView, SearchMobileListView

urlpatterns = [
    path('brand/add/',CreateBrandView.as_view()),
    path('brand/all/',BrandListView.as_view()),
    path('brand/delete/<str:brand>/',DeleteBrandView.as_view()),
    path('add/',CreateMobileView.as_view()),
    path('list/brand/<str:brand>/',MobileListOfBrandView.as_view()),
    path('list/',MobileListView.as_view()),
    path('detail/<str:mobile_id>/',MobileDetailView.as_view()),
    path('update/<str:mobile_id>/',UpdateMobileView.as_view()),
    path('delete/<str:mobile_id>/',DeleteMobileView.as_view()),
    path('search/<str:key>/',SearchMobileListView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
