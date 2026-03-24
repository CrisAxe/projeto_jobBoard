from django.shortcuts import render
from .models import Application

def applications_list(request):
    applications = Application.objects.all()
    return render(request, 'applicationPipeline/applications_list.html', {'applications': applications})

def update_status_view(request, app_id):
  
    return render(request, 'applicationPipeline/update_status.html')