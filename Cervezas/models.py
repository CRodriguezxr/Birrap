from django.db import models



class Cerveza(models.Model):    
    style = models.CharField(max_length=50)
    description = models.CharField(max_length=500,null=True,blank=True)
    alcohol_volume = models.FloatField()
    IBU = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to='Cervezas/', null=True, blank=True)
    is_active = models.BooleanField (default=True)


    def __str__(self):
        return self.style


    class Meta:
        verbose_name = 'Cerveza'
        verbose_name_plural = 'Cervezas'


class Category(models.Model):
    style = models.CharField(max_length=50)



# class Red(models.Model):
#     style = models.CharField (max_length=50,null=True,blank=True)
#     description = models.CharField (max_length=2500,null=True,blank=True)
#     alcohol_volume = models.FloatField (max_length=2,null=True,blank=True)
#     IBU = models.FloatField (max_length=2,null=True,blank=True)
#     price = models.FloatField (default=True, null=True,blank=True)
#     creation_date = models.DateField (auto_now_add=True, null=True, blank=True)
#     is_active = models.BooleanField (default=True)


# class Black(models.Model):
#     style = models.CharField (max_length=50,null=True,blank=True)
#     description = models.CharField (max_length=2500,null=True,blank=True)
#     alcohol_volume = models.FloatField (max_length=2,null=True,blank=True)
#     IBU = models.FloatField (max_length=2,null=True,blank=True)
#     price = models.FloatField (default=True, null=True,blank=True)
#     creation_date = models.DateField (auto_now_add=True, null=True, blank=True)
#     is_active = models.BooleanField (default=True)

