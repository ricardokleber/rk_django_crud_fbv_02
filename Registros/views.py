from django.shortcuts import render, redirect
from .models import Registro
from django.contrib import messages

def home(request):
    registrosListados = Registro.objects.all()
    return render(request, "gestaoRegistros.html", {"registros": registrosListados})

def inserirRegistro(request):
    nome = request.POST['txtNome']
    telefone = request.POST['txtTelefone']
    registro = Registro.objects.create(
        nome=nome, telefone=telefone)
    messages.success(request, 'Registro Inserido')
    return redirect('/')

def editarRegistro(request, id_registro):
    registro = Registro.objects.get(pk = id_registro)
    return render(request, "edicaoRegistro.html", {"registros": registro})

def alterarRegistro(request, id_registro):
    nome = request.POST['txtNome']
    telefone = request.POST['txtTelefone']
    registronovo = Registro.objects.get(pk = id_registro)
    registronovo.nome = nome
    registronovo.telefone = telefone
    registronovo.save()
    messages.success(request, 'Registro alterado')
    return redirect('/')

def deletarRegistro(request, id_registro):
    registro = Registro.objects.get(pk=id_registro)
    registro.delete()
    messages.success(request, 'Registro deletado')
    return redirect('/')
