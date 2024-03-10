from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *
urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('generalapphomepage', views.generalhomepage, name='generalhomepage'),
    path('donatorapphomepage', views.donatorhomepage, name='donatorhomepage'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('donatorapp/successpage',views.successpage,name="successpage"),
    path('phone',views.phone,name="phone"),
    path('insta',views.insta,name="insta"),
    path('linked',views.linked,name="linked"),


]