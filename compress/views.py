from django.shortcuts import render
from django.http import HttpResponse
import random
import os

from compress.forms import UploadForm
from compress.models import UploadModel


# Create your views here.
def index(request):
    return render(request, 'index.html')

def compress(request):
    return render(request, 'compression.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['image']
            model = UploadModel(image=file, image_size=file.size, image_name=file.name, image_format=file.content_type, image_compressed_size=file.size, image_compressed_format=file.content_type, image_compression_ratio=0.0, image_compression_time=0.0, image_compression_status=False, image_compression_psnr=0.0)
            model.save()
            return render(request, 'success.html')
    else:
        form = UploadForm()
    return render(request, 'partials/_upload.html', {'form': form})

