from django.forms import ModelForm
from django.forms import ModelForm
from django import forms
from app.models import user, prod
class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['nome','cnpj','endereco','email','senha']

class prodForm(ModelForm):
    class Meta:
        model = prod
        fields = ['nome','descricao','tipo','valor']