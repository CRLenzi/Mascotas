from django.http import HttpResponse
from django.shortcuts import render


"""aca iran todas las vistas"""

def saludo(request):
	
	return render(request, "index.html")