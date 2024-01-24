from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers



class BrandSerializer(ModelSerializer):
    class Meta:
        model=Brand
        fields=['id','brand_name']

class EoslSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.brand_name', read_only=True)

    class Meta:
        model = Eosl
        fields = ['id', 'brand_name', 'model', 'eosl_date', 'category']
