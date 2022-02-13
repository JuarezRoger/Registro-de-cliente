from django import forms 
from .models import Cliente
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
			'identidad':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.Select(attrs={'class':'form-control'}),
		}

