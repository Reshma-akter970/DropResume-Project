from django import forms
from .models import ResumeModel
GENDER_CHOICES=[
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICES=[
    ('Barisal','Barisal'),
    ('Khulna', 'Khulna'),
    ('Sylhet','Sylhet'),
    ('Rajshahi','Rajshahi'),
    ('Dhaka','Dhaka'),
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model=ResumeModel
        fields=['fname','lname','date_of_birth','gender', 'national','present_address','permanent_address','mobile','email','linkedin','preferred_job','job_type','job_city','profile','my_file']
        labels={'fname':'Full Name','lname':'Last Name','date_of_birth':'Date of Birth','national':'Nationality','profile':'Profile Image','linkedin':'LinkedIn','my_file':'Resume','job_city':'Preferred Job City','job_type':'Job Type'}
        widgets={   
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'national':forms.TextInput(attrs={'class':'form-control'}),
            'present_address':forms.TextInput(attrs={'class':'form-control'}),
            'permanent_address':forms.TextInput(attrs={'class':'form-control'}),
            'preferred_job':forms.TextInput(attrs={'class':'form-control'}),
            'job_type':forms.Select(attrs={'class':'form-control'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control'}),
            'job_city':forms.Select(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),

        }