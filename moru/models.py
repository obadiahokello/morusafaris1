from django.db import models
from django.db.models import CharField
from django.utils.html import mark_safe


# Create your models here.

class service(models.Model):
    heading = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)


class tour(models.Model):
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='media/', default="product.jpg")

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % self.image.url)


class team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100)


class footer(models.Model):
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)


class htels(models.Model):
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=100000000)
    content2 = models.CharField(max_length=100000000, null=True)
    content3 = models.CharField(max_length=100000000, null=True)
    content4 = models.CharField(max_length=100000000, null=True)
    content5 = models.CharField(max_length=100000000, null=True)
    content6 = models.CharField(max_length=100000000, null=True)
    content6 = models.CharField(max_length=100000000, null=True)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='media/', default="product.jpg")
