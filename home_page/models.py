from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

