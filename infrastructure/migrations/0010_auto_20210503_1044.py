# Generated by Django 3.1.6 on 2021-05-03 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0009_auto_20210428_1323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='corpera',
            new_name='corpora',
        ),
        migrations.RenameField(
            model_name='corpora',
            old_name='contactperson',
            new_name='contact',
        ),
    ]