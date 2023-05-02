
from django.shortcuts import render, redirect
from app.forms import userForm,prodForm
from app.models import user, prod
#################################cadastrar login
#from django.contrib.auth.decorators import login_required
#@login_required
##############################menu e login####################################################################
def menu(request):
    return render(request,  "menu.html")
def login(request):
    return render(request,  "login.html")

##############################cadastro empresa########################################################3
def usuario(request):
    data = {}
    data['db'] = user.objects.all()
    return render(request,  "usuario.html",data)

def form(request):
    data= {}
    data ['form'] = userForm()
    return render(request,  "form.html", data)

###########################################banco######################################################################333

def create(request):
    form = userForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("usuario")


def ver(request, pk):
    data = {}
    data['db'] = user.objects.get(pk=pk)
    return render(request, "ver.html", data)

def edit(request, pk):
    data = {}
    data['db'] = user.objects.get(pk=pk)
    data['form'] = userForm(instance=data['db'])
    return render(request,'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = user.objects.get(pk=pk)
    form = userForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect("usuario")

def delete(request, pk):
    db = user.objects.get(pk=pk)
    db.delete()
    return redirect('usuario')

##############################cadastro produto########################################################

def produto(request):
    data = {}
    data['db'] = prod.objects.all()
    return render(request,  "produto.html",data)

def form2(request):
    data = {}
    data['form2'] = prodForm()
    return render(request, "form2.html", data)

###########################################banco######################################################################333

def createprod(request):
    form2 = prodForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        return redirect("produto")



def verproduto(request, pk):
    data = {}
    data['db'] = prod.objects.get(pk=pk)
    return render(request, "verproduto.html", data)

def editproduto(request, pk):
    data = {}
    data['db'] = prod.objects.get(pk=pk)
    data['form2'] = prodForm(instance=data['db'])
    return render(request,'form2.html', data)


def updateproduto(request, pk):
    data = {}
    data['db'] = prod.objects.get(pk=pk)
    form2 = prodForm(request.POST or None, instance=data['db'])
    if form2.is_valid():
        form2.save()
        return redirect("produto")

def deleteproduto(request, pk):
    db = prod.objects.get(pk=pk)
    db.delete()
    return redirect('produto')
