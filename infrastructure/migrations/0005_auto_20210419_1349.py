# Generated by Django 3.1.6 on 2021-04-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0004_auto_20210415_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpera',
            name='contactperson',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='corpera',
            name='way_of_collecting',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='corpera',
            name='word_count',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
