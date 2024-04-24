from rest_framework import serializers
from .models import Book, Category, Publisher, Author


# các chức năng liên quan đến category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['publisher_id', 'name', 'address', 'email', 'phone_number', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


# lưu, xóa book
class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)
    author_id = serializers.CharField(write_only=True)
    publisher_id = serializers.CharField(write_only=True)
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'image', 'price', 'sale', 'quantity', 'des', 'category_id', 'author_id', 'publisher_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        publisher_id = validated_data.pop('publisher_id', None)
        author_id = validated_data.pop('author_id', None)
        image = validated_data.pop('image', None)
        request = self.context.get('request')

        if category_id:
            category_instance = Category.objects.filter(is_active__in=[True], category_id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')

        if author_id:
            author_instance = Author.objects.filter(is_active__in=[True], author_id=author_id).first()
            if author_instance:
                validated_data['author'] = author_instance
            else:
                raise serializers.ValidationError('Author does not exits')

        if publisher_id:
            publisher_instance = Publisher.objects.filter(is_active__in=[True], publisher_id=publisher_id).first()
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
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'image', 'price', 'sale', 'quantity', 'des', 'category', 'author', 'publisher']

class UpdateBookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)
    publisher_id = serializers.CharField(write_only=True)
    author_id = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['title','image', 'price', 'sale','quantity','des','is_active', 'category_id','publisher_id','author_id']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.title = validated_data.get('title')
        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')
        instance.is_active = validated_data.get('is_active')
        instance.des = validated_data.get('des')

        category_id = validated_data.pop('category_id')
        category_instance = Category.objects.filter(is_active__in = [True], category_id=category_id).first()
        if category_instance:
            instance.category = category_instance
        else:
            raise serializers.ValidationError('Category does not exists')
        publisher_id = validated_data.pop('publisher_id')
        publisher_instance = Publisher.objects.filter(is_active__in = [True], publisher_id=publisher_id).first()
        if publisher_instance:
            instance.publisher = publisher_instance
        else:
            raise serializers.ValidationError('Publisher does not exists')
        author_id = validated_data.pop('author_id')
        author_instance = Author.objects.filter(is_active__in=[True], author_id=author_id).first()
        if author_instance:
            instance.author= author_instance
        else:
            raise serializers.ValidationError('Author does not exists')
        instance.save()
        return instance