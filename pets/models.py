from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
  AGE_UNITS = [
    ('day', 'day'),
    ('month', 'Mes'),
    ('year', 'Año')
  ]
  
  COLORS = [
    ('black', 'Negro'),
    ('white', 'Blanco'),
    ('brown', 'Café'),
    ('yellow', 'Amarillo'),
    ('blue', 'Azul'),
    ('green', 'Verde'),
    ('red', 'Rojo')
  ]
  
  SPECIES = [
    ('cat', 'Gato'),
    ('dog', 'Perro'),
    ('bird', 'Ave'),
    ('lizzard', 'Lagarto'),
    ('amphibian', 'Anfibio'),
    ('horse', 'Caballo'),
    ('cow', 'Vaca'),
    ('fish', 'Pez')
  ]
  
  name = models.CharField(max_length=20)
  specie = models.CharField(max_length=15, choices=SPECIES)
  age = models.IntegerField()
  age_unit = models.CharField(max_length=5, choices=AGE_UNITS)
  primary_color = models.CharField(max_length=15, choices=COLORS)
  secondary_color = models.CharField(max_length=15, choices=COLORS)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"name: {self.name}, specie: {self.specie}, age: {self.age}, age_unit: {self.age_unit}"
