# Generated by Django 3.1.6 on 2021-04-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corpera',
            old_name='corpera_discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='corpera',
            old_name='corpera_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='corpera',
            old_name='corpera_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='corpera',
            name='annotated',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='corpera',
            name='anonymization',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='corpera',
            name='category',
            field=models.CharField(choices=[('patientendossier', 'patientendossier'), ('forum', 'forum'), ('richtlijn', 'richtlijn'), ('terminologiestelsel', 'terminologiestelsel'), ('anders', 'anders')], default='patientendossier', max_length=50),
        ),
        migrations.AddField(
            model_name='corpera',
            name='discipline',
            field=models.CharField(choices=[('anders', 'anders'), ('huisarts', 'huisarts')], default='huisarts', max_length=50),
        ),
        migrations.AddField(
            model_name='corpera',
            name='research',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]