from . import views
from django.urls import path

app_name = 'administrador'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('cadastroaluno', views.cadastroAluno, name='cadastro-aluno')
]