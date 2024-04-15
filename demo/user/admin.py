from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "email", )
    search_fields = ("username", "email", )

admin.site.register(User, UserAdmin)