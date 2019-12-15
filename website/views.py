from django.shortcuts import render
from website.models import Usuario, Aluno

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        aluno = Aluno()
        aluno.nome= request.POST.get('nome')
        aluno.email= request.POST.get('email')
        aluno.senha= request.POST.get('senha')
        aluno.frase= request.POST.get('frase')
        aluno.save()
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')
