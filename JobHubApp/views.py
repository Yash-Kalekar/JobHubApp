from django.shortcuts import render, redirect
from .forms import JobForm
from . models import job
# Create your views here.

def home(request):
    return render(request, 'home.html')
def job_creation(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            form = JobForm()
        return render(request, 'job_creation.html', {'form': form})
    else:
        form = JobForm()
        return render(request, 'job_creation.html', {'form': form})
def job_listings(request):
    data = job.objects.all()
    return render(request, 'job_listings.html', {'data': data})
