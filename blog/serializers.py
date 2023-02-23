from rest_framework import serializers
from .models import *

class CatergorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Category
        fields = ("name",)
       
        
    
class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.IntegerField()
    class Meta:
        model = Blog
        fields = ("title","content","image","category", "author", "category_id", "author_id")