from django.db import models

# The corpora model is created here


class corpora(models.Model):
    def __str__(self):
        return 'corpora: ' + self.name
    #categories choices can be changed here
    categories_choices= [('patient records','patient record'),('forum','forum'),('guideline','guideline'),('terminology system','terminology system'),('other','other')]
    #discipline choices can be changed here
    discipline_choices=[('other','other'),('Anesthesiology','Anesthesiology'),('Cardiology','Cardiology'),('Cardiothoracic surgery','Cardiothoracic surgery'),('Dermatology','Dermatology'),('Emergency medicine','Emergency medicine'),('Gastroenterology','Gastroenterology'),('General practitioner','General practitioner'),('Gynaecology','Gynaecology'),('Internal medicine','Internal medicine'),('Medical microbiology','Medical microbiology'),('Neurology','Neurology'),('Neurosurgery','Neurosurgery'),('Nuclear medicine','Nuclear medicine'),('Oncology','Oncology'),('Ophthalmology','Ophthalmology'),('Orthopedics','Orthopedics'),('Otorhinolaryngology','Otorhinolaryngology'),('Pathology','Pathology'),('Pediatrics','Pediatrics'),('Physical medicine and rehabilitation','Physical medicine and rehabilitation'),('Plastic surgery','Plastic surgery'),('Psychiatry','Psychiatry'),('Pulmonology','Pulmonology'),('Radiology','Radiology'),('Rheumatology','Rheumatology'),('Sports medicine','Sports medicine'),('Surgery','Surgery'),('Urology','Urology')]
    #language choices can be changed here
    language_choices=[('Dutch','Dutch'),('English','English'),('German','German'),('French','French')]
    id = models.AutoField(auto_created=True,primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=50, choices=categories_choices , default='patient record')
    discipline = models.CharField(max_length=50, choices=discipline_choices, default='huisarts')
    annotated = models.CharField(max_length=1000, null=True,blank=True)
    anonymization = models.CharField(max_length=1000, null=True, blank=True)
    research = models.CharField(max_length=1000, null=True, blank=True)
    word_count = models.IntegerField( null=True, blank=True)
    contact =models.CharField(max_length=1000, null=True, blank=True)
    way_of_collecting = models.CharField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='uploads', null=True, blank=True)
    language = models.CharField(max_length=100,choices=language_choices, null=True, blank=True)





