from django.db import models

# Create your models here.

class Usuario(models.Model): 
    id_u = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        abstract = True

class Professor(Usuario): 
    rotina = models.CharField(max_length=300 , blank=True , null = True)
    created_at = models.DateTimeField(auto_now_add=True)