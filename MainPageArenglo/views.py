
from django.shortcuts import render
from .forms import Contato_Cliente




def base(request):
    return render(request, 'MainPageArenglo/base.html')

def perfil(request):
    return render(request, 'MainPageArenglo/perfil.html')

def contato(request):
    if request.method == 'GET':
        form  = Contato_Cliente()
        context = {
           'form':form
        }
        return render(request, 'MainPageArenglo/contato.html', context=context)
    elif request.method == 'POST':
        form = Contato_Cliente(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'MainPageArenglo/agradecimento.html')
        else:
            context = {
               'form':form
            }
            return render(request, 'MainPageArenglo/contato.html', context=context)


def arquitetura(request):
    return render(request, 'MainPageArenglo/arquitetura.html')

def hidreletrica(request):
    return render(request, 'MainPageArenglo/hidreletrica.html')

def interiores(request):
    return render(request, 'MainPageArenglo/interiores.html')

def planejamento(request):
    return render(request, 'MainPageArenglo/planejamento.html')

def estrutura(request):
    return render(request, 'MainPageArenglo/estrutura.html')
