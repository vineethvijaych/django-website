from django.db import models

# Create your models here.

class picture(models.Model):
    img=models.ImageField(upload_to="mypics/")

class icon(models.Model):
    img=models.ImageField(upload_to="myicons/")