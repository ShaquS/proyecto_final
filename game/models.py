from django.db import models
import datetime
from user.models import User

# Create your models here.
class Game(models.Model):
    YEAR_CHOICES = []
    for r in range(1880, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    name = models.CharField(max_length=40, default="", verbose_name="Nombre")
    plataform = models.CharField(max_length=40, default="", verbose_name="Plataforma")
    year = models.IntegerField(('Año'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    plot = models.TextField(blank = True, null=True, default="", verbose_name="Descripción")
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING,default="", verbose_name="Autor")


    def __str__(self):
        return f'{self.name}'