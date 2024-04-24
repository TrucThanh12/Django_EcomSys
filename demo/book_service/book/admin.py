from django.contrib import admin
from .models import Book, Category, Author, Publisher
from .forms import BookAdminForm
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)


