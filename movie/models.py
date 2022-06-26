from django.db import models
import datetime
from user.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Movie(models.Model):
    YEAR_CHOICES = []
    for r in range(1880, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    name = models.CharField(max_length=40, default="", verbose_name="Nombre")
    cover = models.ImageField(upload_to='staticfiles/covers/',  null=True, blank=True, verbose_name="Poster")
    director = models.CharField(max_length=40, default="", verbose_name="Director")
    year = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    plot = RichTextField(blank = True, null=True, verbose_name="Trama")
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING,default="", verbose_name="Autor")


    def __str__(self):
        return f'{self.name}'
