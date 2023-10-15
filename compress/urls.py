from django.urls import path
from compress import views

urlpatterns = [
    path('',views.home),
    path('anasayfa', views.home),
    path('compress', views.compress), ]