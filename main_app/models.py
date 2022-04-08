from secrets import choice
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LABEL_CHOICES = (
    ("Food", "food"),
    ("Activity", "activity"),
)

ACTIVE_CHOICES = (
    ("CP", "Couch Potato"),
    ("NAS", "Not As Active"),
    ("A", "Active"),
    ("SOA", "Sort of Active"),
    ("T", "Triathlon"),
)

class Review(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    weather = models.CharField(max_length=100)
    active = models.CharField(max_length=40, choices= ACTIVE_CHOICES)

    def __str__(self):
        return self.name

class Act(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=20, choices = LABEL_CHOICES)
    rating = models.IntegerField()
    price = models.IntegerField()
    location = models.CharField(max_length=100)
    images = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    review = models.ManyToManyField(Review)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

