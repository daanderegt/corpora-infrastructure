# Generated by Django 3.1.6 on 2021-06-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0013_auto_20210503_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpora',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='corpora',
            name='discipline',
            field=models.CharField(choices=[('other', 'other'), ('Anesthesiology', 'Anesthesiology'), ('Cardiology', 'Cardiology'), ('Cardiothoracic surgery', 'Cardiothoracic surgery'), ('Dermatology', 'Dermatology'), ('Emergency medicine', 'Emergency medicine'), ('Gastroenterology', 'Gastroenterology'), ('General practitioner', 'General practitioner'), ('Gynaecology', 'Gynaecology'), ('Internal medicine', 'Internal medicine'), ('Medical microbiology', 'Medical microbiology'), ('Neurology', 'Neurology'), ('Neurosurgery', 'Neurosurgery'), ('Nuclear medicine', 'Nuclear medicine'), ('Oncology', 'Oncology'), ('Ophthalmology', 'Ophthalmology'), ('Orthopedics', 'Orthopedics'), ('Otorhinolaryngology', 'Otorhinolaryngology'), ('Pathology', 'Pathology'), ('Pediatrics', 'Pediatrics'), ('Physical medicine and rehabilitation', 'Physical medicine and rehabilitation'), ('Plastic surgery', 'Plastic surgery'), ('Psychiatry', 'Psychiatry'), ('Pulmonology', 'Pulmonology'), ('Radiology', 'Radiology'), ('Rheumatology', 'Rheumatology'), ('Sports medicine', 'Sports medicine'), ('Surgery', 'Surgery'), ('Urology', 'Urology')], default='huisarts', max_length=50),
        ),
    ]
