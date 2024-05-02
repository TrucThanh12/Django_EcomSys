from rest_framework import serializers
from .models import Book, Category, Publisher, Author


# các chức năng liên quan đến category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'email', 'phone_number', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


# lưu, xóa book
class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True)
    author = serializers.CharField(write_only=True)
    publisher = serializers.CharField(write_only=True)
    class Meta:
        model = Book
        fields = ['title', 'image', 'price', 'sale', 'quantity', 'des', 'category', 'author', 'publisher']

    def create(self, validated_data):
        category = validated_data.pop('category', None)
        publisher = validated_data.pop('publisher', None)
        author = validated_data.pop('author', None)
        image = validated_data.pop('image', None)
        request = self.context.get('request')

        if category:
            category_instance = Category.objects.filter(is_active__in=[True], id=category).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')

        if author:
            author_instance = Author.objects.filter(is_active__in=[True], id=author).first()
            if author_instance:
                validated_data['author'] = author_instance
            else:
                raise serializers.ValidationError('Author does not exits')

        if publisher:
            publisher_instance = Publisher.objects.filter(is_active__in=[True], id=publisher).first()
            if publisher_instance:
                validated_data['publisher'] = publisher_instance
            else:
                raise serializers.ValidationError('Publisher is not exits')
        return Book.objects.create(image=request.FILES.get('image'), **validated_data)

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

# Xem thong tin book
class BookInfoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Book
        #fields = ['id', 'title', 'image', 'price', 'sale', 'quantity', 'des', 'category', 'author', 'publisher', 'type']
        fields = '__all__'
        depth =1

    def get_type(self, obj):
        return "book"


class UpdateBookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True)
    publisher = serializers.CharField(write_only=True)
    author = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['title','image', 'price', 'sale','quantity','des','is_active', 'category','publisher','author']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.title = validated_data.get('title')
        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')
        instance.is_active = validated_data.get('is_active')
        instance.des = validated_data.get('des')

        category_id = validated_data.pop('category')
        category_instance = Category.objects.filter(is_active__in = [True], id=category_id).first()
        if category_instance:
            instance.category = category_instance
        else:
            raise serializers.ValidationError('Category does not exists')
        publisher_id = validated_data.pop('publisher')
        publisher_instance = Publisher.objects.filter(is_active__in = [True], id=publisher_id).first()
        if publisher_instance:
            instance.publisher = publisher_instance
        else:
            raise serializers.ValidationError('Publisher does not exists')
        author_id = validated_data.pop('author')
        author_instance = Author.objects.filter(is_active__in=[True], id=author_id).first()
        if author_instance:
            instance.author= author_instance
        else:
            raise serializers.ValidationError('Author does not exists')
        instance.save()
        return instance