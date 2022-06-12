from django.shortcuts import render, redirect
from .models import blog
# Create your views here.
def home(request):
	b=blog.objects.all()
	return render(request, "index.html",{"blog":b})
 
def registrar(request):
	titulo=request.POST["titulotxt"]
	texto=request.POST["textotxt"]
	autor=request.POST["autortxt"]

	registro=blog.objects.create(titulo=titulo,texto=texto,autor=autor)
	return redirect("/")

def eliminar(request,titulo):
	e=blog.objects.get(titulo=titulo)
	e.delete()
	return redirect("/")

def modificar(request,titulo):
	m=blog.objects.get(titulo=titulo)
	return render(request,"modificar.html",{"blog":m})

def modificarblog(request):
	titulo=request.POST["titulotxt"]
	texto=request.POST["textotxt"]
	autor=request.POST["autortxt"]
	m=blog.objects.get(titulo=titulo)
	m.texto=texto
	m.autor=autor
	m.save()
	return redirect("/")