from django.db import models

# Create your models here.


class Chart(models.Model):
    number = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.number)
