from django.db import models


class Ciudad (models.Model):
    descripcion = models.CharField(max_length=25)

class Genero (models.Model):
    descripcion = models.CharField(max_length=25)

class Especialidad (models.Model):
    descripcion = models.CharField(max_length=25)

class Rol(models.Model):
    nombres = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)

class Paciente(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    numero_telefono = models.CharField(max_length=10)
    idgenero = models.IntegerField
    direccion = models.CharField(max_length=25)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

class Medico(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    numero_telefono = models.CharField(max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    registro = models.CharField(max_length=20)

class Familiar(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    numero_telefono = models.CharField(max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    idpaciente = models.IntegerField
    idparentesco = models.IntegerField
    email = models.CharField(max_length=25)

class Usuario(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    contraseña = models.CharField(max_length=25)
    numero_telefono = models.CharField(max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)


