from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return str(self.id)+", "+self.fullname+", "+self.address