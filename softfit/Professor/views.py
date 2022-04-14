from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Administrador.services import prof_service
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/professor/loginProf/')
def index(request):
    return render(request, 'Professor/inicial.html')

def loginProf(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            id_prof = prof_service.encontra_id(email)
            login(request, user)
            return HttpResponseRedirect(reverse('professor:index'))
        else:
            return render(request, "professor/login.html", {
                "message": "Professor não encontrado!"
            })
    else:
        return render(request, "professor/login.html")

def logout_view(request):
    logout(request)
    return render(request, "homepage/index.html", {
        "message": "Log out realizado!"
    })