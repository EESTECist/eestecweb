from django.shortcuts import render

#look at the models file we have on this folder
from .models import Job




# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
