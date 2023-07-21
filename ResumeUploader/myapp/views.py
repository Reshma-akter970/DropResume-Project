

from django.shortcuts import render,HttpResponseRedirect
from .forms import ResumeForm
from .models import ResumeModel
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'myapp/home.html')
class ResumeView(View):
    
    def get(self, request):
        form=ResumeForm()
        candidate=ResumeModel.objects.all()
        return render(request, 'myapp/resume.html',{'form':form})
    

    def post(self, request):
        form=ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')
    

class Candidate(View):
    def get(self, request,pk):
        info=ResumeModel.objects.get(id=pk)
        return render(request, 'myapp/candidate.html',{'info':info})
    

class AllCandidate(View):
    def get(self, request):
        form=ResumeModel.objects.all()
        return render(request, 'myapp/allcandidate.html',{'form':form})




