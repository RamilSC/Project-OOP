from django.db import models
# Create your models here.

class Device(models.Model):
    brand = models.CharField(max_length=100, blank = False)
    serialno = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=100, blank = False)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.brand, self.description)

class Desktop(Device):
    pass


class Laptop(Device):
    pass

class Mobile(Device):
    pass


