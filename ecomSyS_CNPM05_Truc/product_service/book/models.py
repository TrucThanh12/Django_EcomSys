from django.db import models

class Category(models.Model):
    category_id = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    author_id = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    publisher_id = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.CharField(max_length=7,primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/books')
    price = models.FloatField()
    sale = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

