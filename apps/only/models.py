from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')  

    def __str__(self):
        return self.title


# Create your models here.
