from django.db import models

# Create your models here.
class UploadModel(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=100)
    image_size = models.IntegerField()
    image_url = models.URLField(max_length=200)
    image_format = models.CharField(max_length=100)
    image_compressed = models.ImageField(upload_to='images/')
    image_compressed_size = models.IntegerField()
    image_compressed_url = models.URLField(max_length=200)
    image_compressed_format = models.CharField(max_length=100)
    image_compression_ratio = models.FloatField()
    image_compression_time = models.FloatField()
    image_compression_date = models.DateTimeField(auto_now_add=True)
    image_compression_status = models.BooleanField(default=False)
    image_compression_psnr = models.FloatField(null=True)

    def __str__(self):
        return self.image_name