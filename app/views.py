from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def start(response):
def teste(request):
    return render(request, "testes.html")
    #return HttpResponse("fasfasfdas")
def login(request):
    return render(request, "login.html")
def menu(request):
    return render(request, "menu.html")
def cad_usuario(request):
    return render(request, "cad_usuario.html")
