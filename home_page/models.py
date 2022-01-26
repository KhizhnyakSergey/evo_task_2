from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.email

