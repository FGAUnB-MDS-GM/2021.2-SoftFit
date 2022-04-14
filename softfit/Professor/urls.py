from . import views
from django.urls import path

app_name = 'professor'

urlpatterns = [
    path('',views.index, name = "index"),
    path('loginProf/', views.loginProf, name='login-prof'),
    path("logout", views.logout_view, name="logout"),
]