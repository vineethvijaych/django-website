# Generated by Django 4.2.1 on 2023-07-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_images_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='image1',
            name='image_description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image1',
            name='image_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
