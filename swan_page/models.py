from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images", null=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images", null=False)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Realisation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images", null=False)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Testimony(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", null=False)
    content = models.TextField(blank=True)
    provider = models.CharField(max_length=255)
    rate = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images", null=False)

    def __str__(self):
        return self.name





