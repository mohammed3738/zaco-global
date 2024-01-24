from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=250)
    def __str__(self):
        return self.brand_name
    

    
class Eosl(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    model = models.CharField(max_length=100,null=True,blank=True)
    eosl_date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    category = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.model