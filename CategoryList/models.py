from django.db import models

# Create your models here.
class CategoryList(models.Model):
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    category_id= models.CharField(max_length=255)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)