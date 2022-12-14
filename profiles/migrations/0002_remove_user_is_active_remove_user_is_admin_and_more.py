# Generated by Django 4.1 on 2022-08-19 04:06

import django.core.validators
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='profile_image/%Y/%m'),
        ),
    ]
