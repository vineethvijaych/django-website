from django.db import models

# Create your models here.

class picture(models.Model):
    img=models.ImageField(upload_to="mypics/")
    image_name=models.CharField(max_length=20,null=True)
    image_description=models.CharField(max_length=1000,null=True)

class image(models.Model):
    img=models.ImageField(upload_to="mypics/")
    image_name=models.CharField(max_length=20,null=True)

class image1(models.Model):
    img=models.ImageField(upload_to="mypics/")
    image_name=models.CharField(max_length=30,null=True)
    image_desc=models.CharField(max_length=100,null=True)
    image_description=models.CharField(max_length=1000,null=True)