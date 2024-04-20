

# Create your models here.
# customers/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def _str_(self):
        return self.name