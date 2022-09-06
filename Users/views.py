from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from Users.models import User_profile

from django.contrib.auth import login, logout, authenticate

from Users.forms import User_registration_form,User_edit_form

from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'{username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})


@login_required
def edit_form(request):
    usuario = request.user
    if request.method== "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            # usuario.user = form.cleaned_data["user"]
            usuario.email = form.cleaned_data["email"]
            usuario.password1 = form.cleaned_data["password1"]
            usuario.password2 = form.cleaned_data["password2"]
            usuario.save()

            return render(request, "login")
    else:
        form = User_registration_form(initial={
            # "user":usuario.user,
            "email":usuario.email,
        })
        context = {"form": form}
        return render(request,"users/edit_user.html",context=context)



    

def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.profile)