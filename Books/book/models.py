from django.db import models
# Create your models here.

class user_registration(models.Model):
    name = models.CharField(max_length=20)
    phn = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Library(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=20)
    price = models.IntegerField()


class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

# Create your models here.
