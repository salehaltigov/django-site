from django.db import models


class Registration(models.Model):
    fio = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.fio
