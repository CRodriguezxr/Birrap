from django.db import models



class Comidas(models.Model):    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500,null=True,blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='Comidas/', null=True, blank=True)
    is_active = models.BooleanField (default=True)
    
    


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Comida'
        verbose_name_plural = 'Comidas'


class Category(models.Model):
    style = models.CharField(max_length=50)