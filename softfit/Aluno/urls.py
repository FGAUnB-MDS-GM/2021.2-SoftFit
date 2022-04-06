from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('inicial/<int:id>', views.index, name='index'),
    path('objetivo', views.cadastroObjetivo, name='objetivo')
]
