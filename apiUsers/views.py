from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    return HttpResponse("hello world")
    
def consultarPacientes(request):
    all_entries = models.Paciente.objects.all()
    return HttpResponse(all_entries)