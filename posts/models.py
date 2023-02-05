from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'User_post')
    titel =models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey('Category' , on_delete=models.CASCADE ,related_name='post_categry' )
    

    def __str__(self):
        return f"{self.titel} - {self.author}"
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
