from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CreateCategoryView, CreatePublisherView, CreateAuthorView, AddBookView, CategoryListView, \
    BookListView, BookDetailView, BookListOfCategoryView, SearchBookListView, DeleteBookView, DeleteCategoryView, \
    DeletePublisherView, DeleteAuthorView, UpdateBookView

urlpatterns = [
    path('category/add/', CreateCategoryView.as_view()),
    path('category/all/',CategoryListView.as_view()),
    path('category/delete/<str:category_id>/',DeleteCategoryView.as_view()),
    path('author/add/', CreateAuthorView.as_view()),
    path('author/delete/<str:author_id>/',DeleteAuthorView.as_view()),
    path('publisher/add/', CreatePublisherView.as_view()),
    path('publisher/delete/<str:publisher_id>/',DeletePublisherView.as_view()),
    path('add/', AddBookView.as_view()),
    path('/',BookListView.as_view()),
    path('detail/<str:book_id>/',BookDetailView.as_view()),
    path('list/category/<str:category_id>/', BookListOfCategoryView.as_view()),
    path('search/<str:key>/',SearchBookListView.as_view()),
    path('edit/<str:book_id>',UpdateBookView.as_view()),
    path('delete/<str:book_id>/',DeleteBookView.as_view())

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
