from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category}-{self.title}"
    
    class Meta:
        ordering = ["-create_date"]