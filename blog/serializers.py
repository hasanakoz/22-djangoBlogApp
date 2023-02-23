from rest_framework import serializers
from .models import *

class CatergorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("name",)
       
        
    