from django.db import models

# Create your models here.

class pictures(models.Model):
    img=models.ImageField(upload_to="mypics/")
    product_name=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=100,null=True)
