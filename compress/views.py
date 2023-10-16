from django.shortcuts import render
from django.http import HttpResponse
import random
import os

from compress.forms import UploadForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def compress(request):
    return render(request, 'compression.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        file = request.FILES['image']

        if form.is_valid():
            


        return render(request, 'success.html')
    else:
        form = UploadForm()
    return render(request, 'partials/_upload.html', {'form': form})

# def handle_uploaded_files(file):
#     number = random.randint(1,1000000)
#     # filename _ 112.jpg
#     filename, file_extention = os.path.splitext(file.name)
#     name = filename + "_" + str(number) + file_extention
#     # with open("temp/"+name,"wb+") as destination:
#     #     for chunk in file.chunks():
#     #         destination.write(chunk)