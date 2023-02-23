from django.urls import path
from .views import CategoryView, BlogView

urlpatterns = [
  path('categories/', CategoryView.as_view()),
  path('blogs/', BlogView.as_view())
]