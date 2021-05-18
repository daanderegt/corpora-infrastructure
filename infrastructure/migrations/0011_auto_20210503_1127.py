# Generated by Django 3.1.6 on 2021-05-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0010_auto_20210503_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpora',
            name='category',
            field=models.CharField(choices=[('patient records', 'patient record'), ('forum', 'forum'), ('guideline', 'guideline'), ('terminology system', 'terminology system'), ('other', 'other')], default='patientendossier', max_length=50),
        ),
    ]
