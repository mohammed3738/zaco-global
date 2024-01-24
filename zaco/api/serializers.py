from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers



class BrandSerializer(ModelSerializer):
    class Meta:
        model=Brand
        fields=['id','brand_name']

class EoslSerializer(ModelSerializer):
    class Meta:
        model=Eosl
        fields=['id','model','eosl_date','category']