
from django.shortcuts import redirect, render
from Cervezas.models import Cerveza
from Cervezas.forms import Formulario_cervezas

from django.contrib.auth.decorators import login_required



def detalle_cervezas(request,pk):
    if request.method == 'GET':
        cerveza = Cerveza.objects.get(pk=pk)
        context = {'cerveza':cerveza}
        return render(request, 'Cervezas/detalle_cervezas.html', context=context)

def lista_cervezas(request):
    

            cervezas = Cerveza.objects.all() #Trae todos
            context = {
                'cervezas':cervezas
            }
            return render(request, 'Cervezas/lista_cervezas.html', context=context)


def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Cerveza.objects.create(name = request.POST['name'])
    return render(request, 'Cervezas/primer_formulario.html', context={})

def buscar_cerveza(request):
    search = request.GET['search']
    cerveza = Cerveza.objects.filter(style__icontains=search)  #Trae los que cumplan la condicion
    context = {'cerveza':cerveza}
    return render(request, 'Cervezas/buscar_cervezas.html', context=context)







def crear_cerveza(request):
    if request.user.is_authenticated:
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
    return redirect('login')


def actualizar_cerveza(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = Formulario_cervezas(request.POST)
                if form.is_valid():
                    cerveza = Cerveza.objects.get(id=pk)
                    cerveza.style = form.cleaned_data['style']
                    cerveza.description = form.cleaned_data['description']
                    cerveza.alcohol_volume = form.cleaned_data['alcohol_volume']
                    cerveza.IBU = form.cleaned_data['IBU']
                    cerveza.price = form.cleaned_data['price']
                    cerveza.image = form.cleaned_data['image']
                    cerveza.save()

                    return redirect(lista_cervezas)

            elif request.method == 'GET':
                cerveza = Cerveza.objects.get(id=pk)

                form = Formulario_cervezas(initial={
                                                'style':cerveza.style,
                                                'description':cerveza.description,
                                                "alcohol_volume":cerveza.alcohol_volume,
                                                "IBU":cerveza.IBU,
                                                'price':cerveza.price, 
                                                "image":cerveza.image,})
                context = {'form':form}
                return render(request, 'Cervezas/actualizar_cerveza.html', context=context)
        return redirect('login')
    return redirect('login')




def borrar_cervezas(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser:    
            if request.method == 'GET':
                cerveza = Cerveza.objects.get(pk=pk)
                context = {'cerveza':cerveza}
                return render(request, 'Cervezas/borrar_cervezas.html', context=context)
            elif request.method == 'POST':
                cerveza = Cerveza.objects.get(pk=pk)
                cerveza.delete()
                return redirect(lista_cervezas)
        return redirect('login')
    return redirect('login')





    