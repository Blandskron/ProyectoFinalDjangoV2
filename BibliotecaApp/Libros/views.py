from django.shortcuts import render, redirect
from .models import Libro, Autor
from .forms import LibroForm, AutorForm

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = AutorForm()
    return render(request, 'libros/crear_autor.html', {'form': form})
