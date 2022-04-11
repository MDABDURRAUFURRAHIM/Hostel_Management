from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


# Contact Data Tabil
class Contactme(models.Model):
    name = models.CharField(max_length=50,null=True)
    stduentid = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    departnment = models.TextField(max_length=100,null=True)
    message = models.TextField(max_length=500,null=True)


# Account Data Tabil
class Account(models.Model):
    name = models.CharField(max_length=50,null=True)
    stduentid = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    money = models.FloatField(max_length=100,null=True)
    date = models.TextField(max_length=500,null=True)
    experieddate = models.TextField(max_length=500,null=True)


# Room Data Tabil :
class Room(models.Model):
    name = models.CharField(max_length=50,null=True)
    studentid = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    hallname = models.CharField(max_length=100,null=True)
    roomno = models.TextField(max_length=500,null=True)
    floorno = models.TextField(max_length=500,null=True)


# Seat Cancle Table :

class Seatcancle(models.Model):
    name = models.CharField(max_length=50,null=True)
    studentid = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    hallname = models.CharField(max_length=100,null=True)
    roomno = models.TextField(max_length=500,null=True)
