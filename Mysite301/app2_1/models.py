from django.db import models

# Create your models here

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50)
    contactaddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.fullname+", "+self.contactaddress

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    section = models.CharField(max_length=1)

    def __str__(self):
        return str(self.rollno)+", "+self.fullname+", "+self.standard+", "+self.section


class Staff(models.Model):
    fullname=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

    class Meta:
        db_table='tbl_staffs'
        ordering=['fullname','department']

    def __str__(self):
        return str(self.id)+", "+self.fullname + ", " + self.department


# python manage.py makemigrations (DDL-prepared)
# python manage.py migrate (DDL-execute)

# https://sqliteonline.com/

# makemigrations - Create DDL (Create - code to create new table)
# migrate - Apply DDL on database - Create table on database