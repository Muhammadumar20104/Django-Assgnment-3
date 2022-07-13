from django.db import models
# Create your models here.
class Details(models.Model):
    F_Name = models.CharField(max_length=15)
    Discription = models.CharField(max_length=50)
    price = models.CharField(max_length=11)

    def __str__(self):
        return self.F_Name
