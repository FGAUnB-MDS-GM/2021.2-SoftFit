from . import views
from django.urls import path

app_name = 'administrador'

urlpatterns = [
    path('',views.index,name = 'index')
]