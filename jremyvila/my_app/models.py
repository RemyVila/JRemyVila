from django.db import models
from django.contrib.auth.models import User

                ###### models ######

# Hangman
class HangmanWordBank(models.Model):
    # Define fields
    name = models.CharField(max_length=100)
    hint = models.TextField()

    def __str__(self):
        return self.name

# Login
class UserProfile(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    is_online = models.BooleanField()

    def __str__(self):
        return self.user