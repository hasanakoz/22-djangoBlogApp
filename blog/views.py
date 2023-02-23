from django.shortcuts import render
from .serializers import CatergorySerializer, BlogSerializer
from .models import Category, Blog
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatergorySerializer

class BlogView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()

        else:
            queryset = super().get_queryset().filter(is_published=True)
        
        return queryset