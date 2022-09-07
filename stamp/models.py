from django.db import models
from profiles.models import User

class Stamp(models.Model):
    data = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_challenge = models.BooleanField()


# Create your models here.
