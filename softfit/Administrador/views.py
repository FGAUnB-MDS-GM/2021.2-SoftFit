from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World\nVocê tá na página do Administrador")