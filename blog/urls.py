from django.urls import path
from blog.views import main

urlpatterns = [
    path("", main),
]
