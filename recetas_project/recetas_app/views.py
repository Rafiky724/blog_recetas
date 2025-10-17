from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Receta, Valoracion, Comentario
from .forms import RecetaForm, RegistroUsuarioForm, ComentarioForm
from django.contrib import messages

# Create your views here.
from datetime import datetime

def mi_vista(request):
    return render(request, 'base.html', {'timestamp': datetime.now().timestamp()})

def landing(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'home.html', {'username': username})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'recetas/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'recetas/iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('landing')

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    ya_valorado = False
    
    if request.user.is_authenticated:
        ya_valorado = receta.valoraciones.filter(usuario=request.user).exists()
    
    form = ComentarioForm()
    
    context = {
        'receta': receta,
        'ya_valorado': ya_valorado,
        'form': form
    }
    return render(request, 'recetas/detalle_receta.html', context)

@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_receta = form.save(commit=False)
            nueva_receta.autor = request.user
            nueva_receta.save()
                
            return redirect('detalle_receta', receta_id=nueva_receta.id)
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear_recetas.html', {'form': form})

@login_required
def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.user != receta.autor:
        return redirect('lista_recetas')
    
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/editar_receta.html', {'form': form, 'receta': receta})

@login_required
def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.user == receta.autor:
        receta.delete()
    return redirect('lista_recetas')

@login_required
def valorar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    valoracion, created = Valoracion.objects.get_or_create(usuario=request.user, receta=receta)

    if not created:
        valoracion.delete()

    return redirect('lista_recetas')

@login_required
def crear_comentario(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.receta = receta
            comentario.save()
            return redirect('detalle_receta', receta_id=receta.id)
        
    return redirect(request, 'detalle_receta', receta_id=receta.id)

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id, usuario=request.user)
    receta_id = comentario.receta.id
    if request.method == 'POST':
        comentario.delete()
        return redirect('detalle_receta', receta_id=receta_id)
    return redirect("detalle_receta", receta_id)
