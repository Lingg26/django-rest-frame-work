from django.db import models

# Create your models here.
class CategoryItem(models.Model):
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    category_id = models.CharField(max_length=255)
    image= models.ImageField(upload_to="")
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)