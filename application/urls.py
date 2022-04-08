
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^product/(?P<category>[+a-zA-Z0-9@_-]+)/(?P<name>[+a-zA-Z0-9@_-]+)$',views.product,name="product"),
    path('',views.index, name="index"),
]

