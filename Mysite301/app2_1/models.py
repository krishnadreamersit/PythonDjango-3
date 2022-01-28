from django.db import models

# Create your models here.

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    caddress = models.CharField( max_length=50)

    class Meta:
        db_table='tbl_person'