from multiprocessing import context
from django.shortcuts import redirect, render
from Comidas.models import Comidas
from Comidas.forms import Formulario_comidas

from django.contrib.auth.decorators import login_required


def detalle_comidas(request,pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            comidas = Comidas.objects.get(pk=pk)
            context = {'comidas':comidas}
            return render(request, 'Comidas/detalle_comidas.html', context=context)
    return redirect('login')

@login_required
def crear_comida(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_comidas(request.POST, request.FILES)

            if form.is_valid():
                Comidas.objects.create(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    price = form.cleaned_data['price'],
                    image = form.cleaned_data['image']
                )
                
                return redirect(lista_comidas)

        elif request.method == 'GET':
            form = Formulario_comidas()
            context = {'form':form}
            return render(request, 'Comidas/nueva_comida.html', context=context)
    return redirect('login')

def actualizar_comidas(request, pk):
    if request.method == 'POST':
        form = Formulario_comidas(request.POST)
        if form.is_valid():
            comida = Comidas.objects.get(id=pk)
            comida.name = form.cleaned_data['name']
            comida.price = form.cleaned_data['price']
            comida.description = form.cleaned_data['description']
            comida.stock = form.cleaned_data['stock']
            comida.save()

            return redirect(lista_comidas)

    elif request.method == 'GET':
        comida = Comidas.objects.get(id=pk)

        form = Formulario_comidas(initial={
                                        'name':comida.name,
                                        'price':comida.price, 
                                        'description':comida.description,
                                        'stock':comida.stock})
        context = {'form':form}
        return render(request, 'Comidas/actualizar_comida.html', context=context)


@login_required
def lista_comidas(request):
    if request.user.is_authenticated:

            comidas = Comidas.objects.all() #Trae todos
            context = {
                'comidas':comidas
            }
            return render(request, 'Comidas/lista_comidas.html', context=context)

    return redirect('login')

def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Comidas.objects.create(name = request.POST['name'])
    return render(request, 'Comidas/primer_formulario.html', context={})

def buscar_comida(request):
    search = request.GET['search']
    comida = Comidas.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'comida':comida}
    return render(request, 'Comidas/buscar_comida.html', context=context)

def borrar_comida(request, pk):
    if request.method == 'GET':
        comida = Comidas.objects.get(pk=pk)
        context = {'comida':comida}
        return render(request, 'Comidas/borrar_comidas.html', context=context)
    elif request.method == 'POST':
        comida = Comidas.objects.get(pk=pk)
        comida.delete()
        return redirect(lista_comidas)