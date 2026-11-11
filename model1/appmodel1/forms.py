from django import forms


class UserRegistrationForm(forms.Form): 
    
    ESTADO = [('electrico', 'ELECTRICO'), ('bencinero', 'BENCINERO')]

    marca = forms.CharField()
    modelo = forms.CharField()
    patente = forms.CharField(widget=forms.PasswordInput())
    año = forms.CharField(widget=forms.NumberInput())
    tipo_de_contruccion = forms.CharField(widget=forms.RadioSelect(choices=ESTADO))
    tipo_de_reparacion = forms.CharField(widget=forms.Select())
    fecha = forms.CharField(widget=forms.DateInput())
    descrpcion = forms.CharField(widget=forms.Textarea())

    marca.widget.attrs['class'] = 'form-control'
    modelo.widget.attrs['class'] = 'form-control'
    patente.widget.attrs['class'] = 'form-control'
    año.widget.attrs['class'] = 'form-control'
    tipo_de_contruccion.widget.attrs['class'] = 'form-control'
    tipo_de_reparacion.widget.attrs['class'] = 'form-control'
    fecha.widget.attrs['class'] = 'form-control'
    descrpcion.widget.attrs['class'] = 'form-control'

    def clean_patente(self):
        inputPantente = self.cleaned_data['patente']
        if len (inputPantente) > 8 :
            raise forms.ValidationError("Maximo de caracteres son de 8")