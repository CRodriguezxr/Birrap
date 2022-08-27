from django.http import HttpResponse
from django.shortcuts import render

def Saludo(request):
    return HttpResponse("Hola")

def Home(request):
    context = {
        'name':'Claudio',
        'last_name':'Rodriguez',
    }
    return render(request, 'Home.html', context=context)

def index(request):
    return render(request, 'index.html')