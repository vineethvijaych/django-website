# Generated by Django 4.2.1 on 2023-07-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_icon_sm_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myicons/')),
            ],
        ),
    ]