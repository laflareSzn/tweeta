from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class TweetaaUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    Tweeta_user = models.OneToOneField(TweetaaUser, on_delete=models.CASCADE, primary_key=True)


   
