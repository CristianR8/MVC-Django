from django.shortcuts import render
from .models import project

def view_home(request):
    projects = project.objects.all()
    return render(request, 'view.html', {'projects': projects})


