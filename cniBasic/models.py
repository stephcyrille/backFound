from django.db import models


class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=10)
    city = models.CharField(max_length=50)  
    lat = models.CharField(max_length=10)
    long = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cni(models.Model):
    nberCni = models.IntegerField(unique=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=10)
    address = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nberCni)


class Recep(models.Model):
    nberRecep = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=10)
    address = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nberRecep