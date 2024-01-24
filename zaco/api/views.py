from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializers import *
# from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework import status
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
    
  brand = Brand.objects.all()
  eosl=Eosl.objects.all()
    # filter ends here
    
  branch_serializer = BrandSerializer(brand,many=True)
  eosl_serializer = EoslSerializer(eosl,many=True)


  data = {
        "brand": branch_serializer.data,
        "eosl": eosl_serializer.data,

    }
  return Response(data)