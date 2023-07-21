
# Register your models here.
from django.contrib import admin
from .models import ResumeModel

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','date_of_birth','gender','national','present_address','permanent_address','job_type', 'mobile','job_city','profile','my_file','linkedin','preferred_job']
