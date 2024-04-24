# Generated by Django 4.1.13 on 2024-04-24 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/books')),
                ('price', models.FloatField()),
                ('sale', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.publisher')),
            ],
        ),
    ]