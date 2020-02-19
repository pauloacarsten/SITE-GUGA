from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    # User Counter.
    return render(request, 'home.html')


def singup(request):
        #  User SingUp Form.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html', {
        'form': form,
    })


def portfolio(request):
    return render(request, 'portfolio.html')


def cortes(request):
    return render(request, 'cortes.html')


def cortes2(request):
    return render(request, 'cortes2.html')


def tatuagens(request):
    return render(request, 'tatuagens.html')


def tatuagens2(request):
    return render(request, 'tatuagens2.html')


def desenhos(request):
    return render(request, 'desenhos.html')


def desenhos2(request):
    return render(request, 'desenhos2.html')


def produto(request):
    return render(request, 'produto.html')


def produto2(request):
    return render(request, 'produto2.html')


def contato(request):
    return render(request, 'contato.html')


def perfil(request):
    return render(request, 'perfil.html')


def agendamento(request):
    return render(request, 'agendamento.html')
