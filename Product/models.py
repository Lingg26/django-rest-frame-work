from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    category_id= models.CharField(max_length=255)
    image= models.ImageField(upload_to="")
    time= models.CharField(max_length=255)
    vehicle= models.CharField(max_length=255)
    starting_point= models.CharField(max_length=255)
    destination= models.CharField(max_length=255)
    tour = models.CharField(max_length=10000)
    tour_policy= models.CharField(max_length=10000)
    price= models.IntegerField()
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)