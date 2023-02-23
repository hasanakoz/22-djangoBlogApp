from django.shortcuts import render
from .serializers import CatergorySerializer
from .models import Category
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatergorySerializer