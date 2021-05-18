# Generated by Django 3.1.6 on 2021-04-24 13:20

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0005_auto_20210419_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpera',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/infrastructure/files')),
        ),
    ]