from django.db import models
# Create your models here.


class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    fullname= models.CharField(max_length=50)
    contactaddress = models.CharField(max_length=50)

    class Meta:
        ordering=['pid','fullname', 'contactaddress']

    def __str__(self):
        return str(self.pid)+", "+self.fullname+", "+self.contactaddress