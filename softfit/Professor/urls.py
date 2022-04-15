from . import views
from django.urls import path

app_name = 'professor'

urlpatterns = [
    path('inicial/<int:id>',views.inicial, name = "inicial"),
    path('loginProf/', views.loginProf, name='login-prof'),
    path("logout", views.logout_view, name="logout"),
]