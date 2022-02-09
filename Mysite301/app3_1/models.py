from django.db import models

# Create your models here.

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.name+", "+self.address
