import tempfile

import numpy as np
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse
import random
import os
import cv2 as cv

from compress.forms import UploadForm
from compress.models import UploadModel
from .jpeg_compression import analyze_image


# Create your views here.
def index(request):
    return render(request, 'index.html')


def compress(request):
    return render(request, 'compression.html')


def upload(request):
    quantization_tables = load_quantization_tables()
    compress = UploadModel.objects.all()

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['image']
            model = UploadModel(image=file, image_size=file.size, image_name=file.name, image_format=file.content_type,
                                image_compressed_size=file.size, image_compressed_format=file.content_type,
                                image_compression_ratio=0.0, image_compression_time=0.0, image_compression_status=False,
                                image_compression_psnr=0.0)
            model.save()

            # JPEG sıkıştırma işlemi
            img_path = model.image.path
            block_size = 8
            num_coefficients = 10
            color = True  # Görüntü rengarenkse True, siyah beyazsa False (Varsayılan olarak True)

            # Seçilen kuantalama tablosunu al
            selected_quantization_table = request.POST.get('quantization-table')

            # Seçilen tabloyu kullanarak JPEG sıkıştırma işlemini yap
            if selected_quantization_table is not None:
                selected_table = np.array(quantization_tables[int(selected_quantization_table) - 1], dtype=np.float32)
                print("seçildi",selected_table)
            else:
                # Kuantalama tablosu seçilmediğinde varsayılan bir değer atayabilir veya hata mesajı gösterebilirsiniz.
                # Örnek olarak, varsayılan değeri -1 olarak atayabilirsiniz:
                print("Kuantalama tablosu seçilmedi. Varsayılan tablo kullanılacak.", quantization_tables[0])
                selected_table = np.array(quantization_tables[0], dtype=np.float32)

            original_img, compressed_img, psnr, compression_ratio, encoded_img, color = analyze_image(img_path,
                                                                                                      block_size,
                                                                                                      num_coefficients,
                                                                                                      color, selected_table)

            # Sıkıştırılmış görüntüyü modelde sakla
            # Geçici bir dosyaya sıkıştırılmış görüntüyü kaydet
            # Sıkıştırılmış görüntüyü modelde sakla
            # Geçici bir dosyaya sıkıştırılmış görüntüyü kaydet
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                cv.imwrite(temp_file.name, compressed_img)

            # Sıkıştırılmış görüntüyü modelde sakla
            with open(temp_file.name, 'rb') as compressed_img:
                model.image_compressed.save(model.image_name, File(compressed_img))



            model.image_compressed_size = os.path.getsize(model.image_compressed.path)
            model.image_compressed_format = "image/jpeg"  # Varsayılan sıkıştırma formatı olarak JPEG kullanılıyor
            model.image_compression_ratio = compression_ratio
            model.image_compression_psnr = psnr
            model.image_compression_status = True

            model.save()

            return render(request, 'partials/_upload.html',
                          {'compress': compress, 'original_img': original_img, 'compressed_img': compressed_img,
                           'psnr': psnr, 'compression_ratio': compression_ratio})
    else:
        form = UploadForm()
    return render(request, 'partials/_upload.html', {'form': form, 'quantization_tables': quantization_tables})


import json


def load_quantization_tables():
    # JSON dosyasını okuyun
    with open('static/compress/data/veri.json', 'r') as json_file:
        quantization_data = json.load(json_file)

    return quantization_data
