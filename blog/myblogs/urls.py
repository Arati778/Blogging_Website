from django.contrib import admin
from django.urls import path,include
from .views import home,post,category

urlpatterns = [
    path('',home),
    path('<slug:url>',post),
    path('myblogs<slug:url>',category),

]