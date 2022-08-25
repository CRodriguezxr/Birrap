from django.http import HttpResponse
from django.shortcuts import render, redirect

def saludo(request):
    return HttpResponse("Hola")

def segundo_template(request):
    context = {
        'name':'Luca',
        'last_name':'Citta Giordano',
    }
    return render(request, 'Home.html', context=context)