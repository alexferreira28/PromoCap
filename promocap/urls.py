"""promocap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import form, usuario, create, ver, update, edit, delete, produto, form2, menu, login,createprod, verproduto, editproduto, updateproduto, deleteproduto
urlpatterns = [

    #path('accounts/', include('django.contrib.auth.urls')),
    path('admin', admin.site.urls,name= 'admin'),


    path('menu', menu, name='nemu'),
    path('login', login, name='login'),
    ############################usuario#########################################
    path('usuario', usuario, name='usuario'),
    path('form', form, name='form'),
    path('create', create, name= 'create'),
    path('ver<int:pk>', ver, name='ver'),
    path('edit<int:pk>', edit, name='edit'),
    path('update<int:pk>', update, name='update'),
    path('delete<int:pk>', delete, name='delete'),
    #################################produto######################################
    path('produto', produto, name='produto'),
    path('form2', form2, name='form2'),
    path('createprod', createprod, name='createprodproduto'),
    path('verproduto<int:pk>', verproduto, name='verproduto'),
    path('editproduto<int:pk>', editproduto, name='editproduto'),
    path('updateproduto<int:pk>', updateproduto, name='updateproduto'),
    path('deleteproduto<int:pk>', deleteproduto, name='deleteproduto'),

    #path('accounts'.include('django.contrib.auth.urls')),
    #path('createprod', createprod, name='createprod'),

]


