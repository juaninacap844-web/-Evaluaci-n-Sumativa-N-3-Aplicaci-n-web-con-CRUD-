from django.shortcuts import render
from . import forms
from django.db.models import Prefetch
from appmodel1.models import *
from appmodel1.forms import UserRegistrationForm

def userRegistrationView (request):
    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Marca: ", form.cleaned_data{'marca'})
            print("Modelo: ", form.cleaned_data{'modelo'})
            print("Patente: ", form.cleaned_data{'patente'})
            print("Año: ", form.cleaned_data{'año'})
            print("Tipo de Combustible: ", form.cleaned_data{'tipo_de_combusible'})
            print("Tipo de Reaparcion: ", form.cleaned_data{'tipo_de_reparacion'})
            print("Fecha de Ingreso: ", form.cleaned_data{'fecha_de_ingreso'})
            print("Descripcion: ", form.cleaned_data{'descripcion'})
        data = {'form' : form}
        return render (request, 'formulario.html', data)