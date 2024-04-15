from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, default=0)
    is_active = models.BooleanField(default=True)

    # thay đổi tham số related_name trong địng nghĩa các trường groups và user_permission để phân biệt
    # giữa các liên kết ngược cho model User và AbstractUser
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name="user",
        related_name="custom_user_set",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name="user",
        related_name="custom_user_set",
    )

    def __str__(self):
        return self.username
