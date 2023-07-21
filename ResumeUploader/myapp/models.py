from django.db import models
DIVISION_CHOICE=(
    ('Barisal','Barisal'),
    ('Mymensingh', 'Mymensingh'),
    ('Khulna', 'Khulna'),
    ('Chattogram','Chattogram'),
    ('Sylhet','Sylhet'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Dhaka','Dhaka'),
)
TYPE_CHOICE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Contract','Contract'),
)


# Create your models here.
class ResumeModel(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=200)
    national=models.CharField(max_length=200)
    present_address=models.TextField() 
    permanent_address=models.TextField() 
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_type=models.CharField(choices=TYPE_CHOICE,max_length=100)
    preferred_job=models.CharField(max_length=250)
    job_city=models.CharField(choices=DIVISION_CHOICE, max_length=100)
    linkedin=models.URLField( blank=True)
    profile=models.ImageField(upload_to='profileimage', blank=True) 
    my_file=models.FileField(upload_to='resumefile', blank=True)