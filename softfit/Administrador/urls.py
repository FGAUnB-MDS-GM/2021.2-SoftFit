from . import views
from django.urls import path

app_name = 'administrador'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('cadastroaluno', views.cadastroAluno, name='cadastro-aluno'),
    path('cadastroprofessor', views.cadastroProfessor, name='cadastro-professor'),
    path('mostraaluno/<int:id>', views.mostraAluno, name='mostra-aluno'),
    path('editaraluno/<int:id>', views.editaAluno, name='edita-aluno'),
    path('editarprof/<int:id>', views.editaProfessor, name='edita-prof'),
    path('removeraluno/<int:id>', views.removeAluno, name='remove-aluno'),
    path('removerprof/<int:id>', views.removeProfessor, name='remove-prof')
]