from django.shortcuts import render
from website.models import Aluno

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    contexto ={}
    if request.method == 'POST':
        aluno = Aluno()
        aluno.nome= request.POST.get('nome')
        aluno.email= request.POST.get('email')
        aluno.senha= request.POST.get('senha')
        aluno.frase= request.POST.get('frase')
        aluno.save()
        return render(request, 'home.html')
    return render(request, 'cadastro.html')