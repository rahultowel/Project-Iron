from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class PollUser(User):
    """docstring for PollUser."""
    spirit_animal=models.CharField(max_length=100, default='AnimalsSuck')


class Notify(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    not_text=models.CharField(max_length=200)
    not_memo=models.CharField(max_length=100) #user name of the notifier
    readStatus=models.BooleanField(default=False)
    typePerm=models.BooleanField(default=False)

    def __str__(self):
        return self.not_text[:10]
