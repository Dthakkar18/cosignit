from django.db import models

# Create your models here.

class Member(models.Model):
    firstName = models.CharField(max_length=225)
    lastName = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    password = models.CharField(max_length=225)
    birthday = models.DateField()

    def __str__(self):
        return self.firstName + " " + self.lastName
