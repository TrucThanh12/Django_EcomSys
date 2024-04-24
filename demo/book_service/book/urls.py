from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CreateCategoryView, CreatePublisherView, CreateAuthorView, AddBookView, CategoryListView, \
    BookListView, BookDetailView, BookListOfCategoryView, SearchBookListView, DeleteBookView, DeleteCategoryView, \
    DeletePublisherView, DeleteAuthorView, UpdateBookView

urlpatterns = [
    path('api/ecomSys/category/add/', CreateCategoryView.as_view()),
    path('api/ecomSys/category/all/',CategoryListView.as_view()),
    path('api/ecomSys/category/delete/<str:category_id>/',DeleteCategoryView.as_view()),
    path('api/ecomSys/author/add/', CreateAuthorView.as_view()),
    path('api/ecomSys/author/delete/<str:author_id>/',DeleteAuthorView.as_view()),
    path('api/ecomSys/publisher/add/', CreatePublisherView.as_view()),
    path('api/ecomSys/publisher/delete/<str:publisher_id>/',DeletePublisherView.as_view()),
    path('api/ecomSys/book/add/', AddBookView.as_view()),
    path('api/ecomSys/book/all/',BookListView.as_view()),
    path('api/ecomSys/book/detail/<str:book_id>/',BookDetailView.as_view()),
    path('api/ecomSys/book/category/<str:category_id>/', BookListOfCategoryView.as_view()),
    path('api/ecomSys/book/search/<str:key>/',SearchBookListView.as_view()),
    path('api/ecomSys/book/edit/<str:book_id>',UpdateBookView.as_view()),
    path('api/ecomSys/book/delete/<str:book_id>/',DeleteBookView.as_view())

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
