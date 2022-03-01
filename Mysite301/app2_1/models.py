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


class Client(models.Model):
    full_name = models.CharField(max_length=50, help_text="Enter Fullname : ")
    contact_address = models.CharField(max_length=50, help_text="Enter Address : ")
    class Meta:
        db_table = 'tbl_client'
        ordering = ['-id','full_name']
    def __str__(self):
        return str(self.id)+", "+self.full_name.upper()+", "+self.contact_address.upper()


# One to One Relationship
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


# One to Many Relationship
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class News(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ['headline']


# Many to Many Relationship
class Publication(models.Model):
    title = models.CharField(max_length=30)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    class Meta:
        ordering = ['headline']
    def __str__(self):
        return self.headline

# python manage.py makemigrations (DDL-prepared)
# python manage.py migrate (DDL-execute)
# https://sqliteonline.com/
# makemigrations - Create DDL (Create - code to create new table)
# migrate - Apply DDL on database - Create table on database