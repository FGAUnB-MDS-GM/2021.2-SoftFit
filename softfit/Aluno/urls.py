from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.index, name='index'),
]
