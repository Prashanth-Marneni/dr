from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    leftimg = models.ImageField(upload_to='images/')
    rightimg = models.ImageField(upload_to='images/')
    leftdr = models.CharField(max_length=50)
    rightdr = models.CharField(max_length=50)
    def __str__(self):
        return self.name