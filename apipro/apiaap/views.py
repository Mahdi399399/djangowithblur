from django.shortcuts import render

# Create your views here.
from . import views
from rest_framework import routers
from django.urls import path, include
router=routers.DefaultRouter()
router.register('awsimage',views.awsimageview)
urlpatterns=[
    path('',include(router.urls))
]


