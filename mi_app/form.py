from django import forms

class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Nombre',
        'data-sb-validations': 'required'
    }))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Apellido',
        'data-sb-validations': 'required'
    }))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Correo electronico',
        'data-sb-validations': 'required,correo'
    }))

    
class BuscarForm(forms.Form):
    correo = forms.EmailField(label='Email del estudiante', required=True)