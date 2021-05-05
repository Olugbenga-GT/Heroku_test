from django.db import models
from User.models import  User

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='gallery/Post/')
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.text
