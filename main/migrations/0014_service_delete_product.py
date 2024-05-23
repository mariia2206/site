# Generated by Django 4.2.9 on 2024-05-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_name_action_author2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('full_description', models.TextField()),
                ('photo', models.ImageField(upload_to='services_photos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]