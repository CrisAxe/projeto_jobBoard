from django.shortcuts import render
from .models import Application

def applications_list(request):
    return render(request, 'applicationPipeline/application_list.html')

def update_status_view(request, app_id):
  
    return render(request, 'applicationPipeline/update_status.html')