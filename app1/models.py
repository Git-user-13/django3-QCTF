from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

SCORE_CHOICES = ( 
    (10, 10), 
    (20, 20),
    (30, 30),
    (40, 40),
    (50, 50),
    (60, 60),
    (70, 70),
    (80, 80),
    (90, 90),
    (100, 100),
 )

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    hint_1 = models.CharField(max_length=200, blank=True)
    flag_1 = models.CharField(max_length=200, blank=True)
    hint_2 = models.CharField(max_length=200, blank=True)
    flag_2 = models.CharField(max_length=200, blank=True)
    hint_3 = models.CharField(max_length=200, blank=True)
    flag_3 = models.CharField(max_length=200, blank=True)
    hint_4 = models.CharField(max_length=200, blank=True)
    flag_4 = models.CharField(max_length=200, blank=True)
    hint_5 = models.CharField(max_length=200, blank=True)
    flag_5 = models.CharField(max_length=200, blank=True)

    
class Flag(models.Model):
    q1 = models.IntegerField(max_length=200, blank=True)
    h1 = models.CharField(max_length=200, blank=True)
    f1 = models.CharField(max_length=200, blank=True)
    h2 = models.CharField(max_length=200, blank=True)
    score = models.IntegerField(choices = SCORE_CHOICES, blank=True, default= 10)
    f2 = models.CharField(max_length=200, blank=True)
    h3 = models.CharField(max_length=200, blank=True)
    f3 = models.CharField(max_length=200, blank=True)
    h4 = models.CharField(max_length=200, blank=True)
    f4 = models.CharField(max_length=200, blank=True)
    h5 = models.CharField(max_length=200, blank=True)
    f5 = models.CharField(max_length=200, blank=True)

class complete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hint = models.ForeignKey(Flag, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    finished_at = models.DateTimeField(default=datetime.now)

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('index')