from django.db import models

# Create your models here.

cat = (('School','School'),('Collage','Collage'),('Restaurants','Restaurants'))
class Categories(models.Model):
    category = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='pics/',default='default.jpg')
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=250)

class Ads(models.Model):
    category = models.CharField(max_length=50,choices=cat,default='School')
    brand = models.CharField(max_length=50,unique=True)
    about = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='images/',default='default.jpg')

class Member(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    mobile = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='pics',default='default.jpg')
