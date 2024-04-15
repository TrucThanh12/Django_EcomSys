from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import SearchView,ShowSearchView,DeleteSearchView
from ecomSyS_CNPM05_Truc.book_service.book import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecomSys/search/', SearchView.as_view()),
    path('api/ecomSys/search/show/', ShowSearchView.as_view()),
    path('api/ecomSys/search/delete/<str:key>/', DeleteSearchView.as_view())
]