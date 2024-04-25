from rest_framework import serializers
from .models import Brand, Mobile


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_id', 'name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class MobileSerializer(serializers.ModelSerializer):
    brand_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['mobile_id', 'title', 'image', 'price', 'sale', 'quantity', 'color', 'size', 'memory', 'ram', 'cpu',
                  'pin','des','brand_id']

    def create(self, validated_data):
        brand_id = validated_data.pop('brand_id',None)
        image = validated_data.pop('image', None)
        request = self.context.get('request')

        if brand_id:
            brand_instance = Brand.objects.filter(is_active__in=[True],brand_id=brand_id).first()
            if brand_instance:
                validated_data['brand_id'] = brand_instance
            else:
                raise serializers.ValidationError('Brand does not exist')
        return Mobile.objects.create(image=request.FILES.get('image'),**validated_data)

    def destroy(self,instance):
        instance.is_active = False
        instance.save()
        return instance

class MobileInfoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Mobile
        fields = ['mobile_id', 'title', 'image', 'price', 'sale', 'quantity', 'color', 'size', 'memory', 'ram', 'cpu',
                  'pin', 'des', 'brand_id','type']

    def get_type(self,obj):
        return "mobile"

class UpdateMobileSerializer(serializers.ModelSerializer):
    brand_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['image',
                  'price',
                  'sale',
                  'quantity',
                  'des',
                  'brand_id']

    def update(self,instance,validated_data):
        request = self.context.get('request')
        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')
        brand_id = validated_data.get('brand_id')
        instance.des = validated_data.get('des')
        brand_instance = Brand.objects.filter(is_active__in=[True], brand_id=brand_id).first()
        if brand_instance:
            instance.brand = brand_instance
        else:
            raise serializers.ValidationError('Brand does not exist')

        instance.save()
        return instance
