from django.db import models

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=50)
    contact_address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.full_name+", "+self.contact_address
