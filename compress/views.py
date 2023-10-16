from django.shortcuts import render
from django.http import HttpResponse
import random
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def compress(request):
    return render(request, 'compression.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES['image']
        print(file)
        handle_uploaded_files(file)
        return render(request, 'success.html')
    return render(request, 'upload.html')

def handle_uploaded_files(file):
    number = random.randint(1,1000000)
    # filename _ 112.jpg
    filename, file_extention = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extention
    with open("temp/"+name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)