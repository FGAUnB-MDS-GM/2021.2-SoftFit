# Generated by Django 4.0.3 on 2022-04-04 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadofinanceiro',
            name='d_pagamento',
        ),
    ]