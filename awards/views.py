from django.shortcuts import render
from .models import Profile, Projects

# Create your views here.


def welcome(request):
    return render(request, 'test.html')

def home(request):
  projects = Projects.get_all()
  title = 'test'

  return render(request, 'awards/home.html', {'projects': projects, "title":title})
