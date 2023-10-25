from django.urls import path
from compress import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.upload, name='index'),
    path('index', views.index, name='home'),
    path('upload', views.upload, name='upload_image'),
    path('compress', views.compress, name='compress'), ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)