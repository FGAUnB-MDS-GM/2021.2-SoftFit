from . import views
from django.urls import path

app_name = 'professor'

urlpatterns = [
    path('',views.index, name = "index")
]