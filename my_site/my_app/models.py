from django.db import models

# Create your models here.

class patient (models.Model):
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)


    

