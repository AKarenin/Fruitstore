from django.db import models

class FruitStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phoneNumber = models.IntegerField(max_length=11)

    def __str__(self):
        return f"{self.name}"


