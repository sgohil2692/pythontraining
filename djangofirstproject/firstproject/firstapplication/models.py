from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20,unique=True)
    ID=models.AutoField(primary_key=True)
    contact=models.IntegerField()
    address=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Musician(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    instrument=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    release_date=models.DateField()
    num_stars=models.IntegerField()

    def __str__(self):
        return str(self.name)