from django.shortcuts import render, redirect
from .models import Libros
from .forms import LibroForm

# Create your views here.

def inicio(request):

    return render(request, "paginas/inicio.html")

def libros(request):

    libros = Libros.objects.all()

    return render(request, 'libros/index.html', {"libros": libros})

def crearLibro(request):

    formulario = LibroForm(request.POST or None , request.FILES or None)

    if formulario.is_valid():

        formulario.save()
        return redirect('libros')

    return render(request, 'libros/crear.html', {'formulario': formulario})

def editarLibro(request, id):

    libro = Libros.objects.get(id = id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance = libro)

    if formulario.is_valid():

        formulario.save()
        return redirect('libros')

    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminarLibro(request, id): 

    libro = Libros.objects.get(id = id)
    libro.delete()

    return redirect('libros')

