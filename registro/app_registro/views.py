from django.shortcuts import render, redirect, get_object_or_404
from .form import ClienteForm
from .models import Cliente
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate



def index(request, id=None):
	cliente = Cliente.objects.all().order_by('identidad')

	if request.method == 'GET':
		clientes = get_object_or_404(Cliente, pk=id) if id else None
		form = ClienteForm(instance=clientes)

		ctx =  {'form':form,
				'cliente':cliente,
				'id':id
				}

		return render(request, 'registro/index.html', ctx)
	else:
		clientes = get_object_or_404(Cliente, pk=id) if id else None
		form = ClienteForm(data=request.POST or None, instance=clientes) 

		if form.is_valid():
			form.save()

			if id:
				messages.add_message(request, messages.SUCCESS, 'Se ha actualizado el cliente con exito')
			else:
				messages.add_message(request, messages.SUCCESS, 'Se ha registrado el cliente con exito')
			

			return redirect('/registro')
		else:
			return render(request, 'index.html', {'form':form, 'cliente':cliente})


def eliminar(request, id):
	clie = Cliente.objects.get(pk=id)
	nombre = clie.nombre

	clie.delete()
	messages.add_message(request, messages.INFO, f'Se ha eliminado {nombre} con exito')
	return redirect('/registro')
