# Generated by Django 4.2.9 on 2024-05-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_photo_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=100),
        ),
    ]
