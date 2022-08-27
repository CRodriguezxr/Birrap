from multiprocessing import context
from django.shortcuts import redirect, render
from Cervezas.models import Cerveza
from Cervezas.forms import Formulario_cervezas

from django.contrib.auth.decorators import login_required


@login_required
def crear_cerveza(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_cervezas(request.POST, request.FILES)

            if form.is_valid():
                Cerveza.objects.create(
                    style = form.cleaned_data['style'],
                    description = form.cleaned_data['description'],
                    alcohol_volume = form.cleaned_data['alcohol_volume'],
                    IBU = form.cleaned_data['IBU'],
                    price = form.cleaned_data['price'],
                    image = form.cleaned_data['image']
                )
                
                return redirect(lista_cervezas)

        elif request.method == 'GET':
            form = Formulario_cervezas()
            context = {'form':form}
            return render(request, 'Cervezas/nueva_cerveza.html', context=context)
    return redirect('login')

def actualizar_cerveza(request, pk):
    if request.method == 'POST':
        form = Formulario_cervezas(request.POST)
        if form.is_valid():
            cerveza = Cerveza.objects.get(id=pk)
            cerveza.name = form.cleaned_data['name']
            cerveza.price = form.cleaned_data['price']
            cerveza.description = form.cleaned_data['description']
            cerveza.stock = form.cleaned_data['stock']
            cerveza.save()

            return redirect(lista_cervezas)

    elif request.method == 'GET':
        cerveza = Cerveza.objects.get(id=pk)

        form = Formulario_cervezas(initial={
                                        'name':cerveza.name,
                                        'price':cerveza.price, 
                                        'description':cerveza.description,
                                        'stock':cerveza.stock})
        context = {'form':form}
        return render(request, 'Cervezas/actualizar_cerveza.html', context=context)


@login_required
def lista_cervezas(request):
    if request.user.is_authenticated:

            cervezas = Cerveza.objects.all() #Trae todos
            context = {
                'cervezas':cervezas
            }
            return render(request, 'Cervezas/lista_cervezas.html', context=context)

    return redirect('login')

def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Cerveza.objects.create(name = request.POST['name'])
    return render(request, 'Cervezas/primer_formulario.html', context={})

def buscar_cerveza(request):
    search = request.GET['search']
    cerveza = Cerveza.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'cerveza':cerveza}
    return render(request, 'Cervezas/buscar_cervezas.html', context=context)

def borrar_cervezas(request, pk):
    if request.method == 'GET':
        cerveza = Cerveza.objects.get(pk=pk)
        context = {'cerveza':cerveza}
        return render(request, 'Cervezas/borrar_cervezas.html', context=context)
    elif request.method == 'POST':
        cerveza = Cerveza.objects.get(pk=pk)
        cerveza.delete()
        return redirect(lista_cervezas)