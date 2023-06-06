from rest_framework import serializers

from .models import Product, Category, Gender, Size


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gender
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Size
        fields = '__all__'

