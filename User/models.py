from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    image = models.ImageField(upload_to= "gallery/User/")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.username