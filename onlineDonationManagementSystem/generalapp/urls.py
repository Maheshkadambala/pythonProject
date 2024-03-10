from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('charity',views.charitypost,name='charitypost'),
    path('add_charity_details',views.add_charity_details,name='add_charity_details'),
    path('viewdetails',views.view_charity_detail,name='view_charity_detail'),
    path('about',views.about,name='about'),
    path("deletecharity/<int:pk>", views.deletecharity, name="deletecharity"),
]