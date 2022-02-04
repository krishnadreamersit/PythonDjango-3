from django.db import models

# Create your models here

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50)
    contactaddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.fullname+", "+self.contactaddress

# Makemigrations - Create DDL (Create - code to create new table)
# Migrate - Apply DDL on database - Create table on database

