from django.db import models

class Настройка(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

#class books(models.Model):
#    date = models.DateField(auto_now_add=True)
