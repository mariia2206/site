# Generated by Django 4.2.9 on 2024-05-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_author2_action_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(),
        ),
    ]
