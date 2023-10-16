from django.urls import path
from compress import views

urlpatterns = [
    path('',views.compress, name='index'),
    path('index', views.index, name='home'),
    path('upload', views.upload, name='upload_image'),
    path('compress', views.compress, name='compress'), ]