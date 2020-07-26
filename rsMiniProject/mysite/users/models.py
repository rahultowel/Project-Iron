from django.db import models
from django.contrib.auth.models import User

class PollUser(User):
    """docstring for PollUser."""
    spirit_animal=models.CharField(max_length=100, default='AnimalsSuck')
