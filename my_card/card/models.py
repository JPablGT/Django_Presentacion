from django.db import models
class Card(models.Model):
    # Campos del modelo
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.EmailField()
    ciudad = models.EmailField()
    email = models.EmailField()
    mensaje = models.CharField(max_length=800)

    def __str__(self):
        return f"datos de la persona: {self.nombres} {self.apellidos} {self.telefono} {self.ciudad} {self.email} {self.mensaje}"
