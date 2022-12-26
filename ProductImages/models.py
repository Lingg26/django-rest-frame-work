from django.db import models
from django.conf import settings
# Create your models here.
class ProductImage(models.Model):
    product_id= models.CharField(max_length=255)
    image= models.ImageField(upload_to="")
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)