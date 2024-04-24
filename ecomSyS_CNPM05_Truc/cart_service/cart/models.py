from django.db import models

class CartItem(models.Model):
    user_id = models.CharField(max_length=7)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    type = models.CharField(max_length=50,null=True)
    product_id = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)