from django.db import models

# Create your models here.

class username(models.Model):
    uname= models.CharField(max_length=100,null=True,blank=True)
    password= models.IntegerField(null=True,blank=True)



    def __int__(self):
        return self.id