from django.db import models

# Modelo para Auditores
class Auditor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Auditados
class Auditado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Sectores
class Sector(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Entregable
class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechaDeAuditoria = models.DateField()
    auditoria_ok = models.BooleanField(default=False)
    auditoria_ng = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


