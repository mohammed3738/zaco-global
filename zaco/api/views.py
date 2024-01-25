from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializers import *
# from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework import status
from collections import defaultdict

# Create your views here.

@api_view(['GET'])
def home(request):
    routes=[
       {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "is_student": False,
    "address": {
      "street": "123 Main Street",
      "city": "Anytown",
      "zipcode": "12345"
    },
    "hobbies": ["reading", "hiking", "photography"]
        }
    ] 
    return Response(routes)



@api_view(['GET'])
def view_eosl(request):
    brands = Brand.objects.all()
    eosls = Eosl.objects.all()

    # Creating a dictionary to organize Eosl instances by brand name
    brand_eosls_dict = defaultdict(list)

    for eosl in eosls:
        brand_eosls_dict[eosl.brand.brand_name].append(EoslSerializer(eosl).data)

    # Creating a list to hold each brand's data
    brand_data_list = []
    for brand in brands:
        brand_data = {
            "brand": BrandSerializer(brand).data,
            "eosls": brand_eosls_dict[brand.brand_name],
        }
        brand_data_list.append(brand_data)

    return Response(brand_data_list)



@api_view(['GET'])
def detail_view_eosl(request):
    # brands = Brand.objects.all()

    eosls = Eosl.objects.filter(brand__brand_name="HP").values('brand','model','eosl_date','category')
    eosl_serializer=EoslSerializer(eosls,many=True)
    data={
        'eosls':eosl_serializer.data
    }
    print(data)

  

    return Response(data)


