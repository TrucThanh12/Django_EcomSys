from django.urls import path
from .views import SearchView,ShowSearchView,DeleteSearchView
from demo.book_service.book import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecomSys/search/', SearchView.as_view()),
    path('api/ecomSys/search/show/', ShowSearchView.as_view()),
    path('api/ecomSys/search/delete/<str:key>/', DeleteSearchView.as_view())
]