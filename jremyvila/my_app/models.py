from django.db import models

# Create your models here.
class HangmanWordBank(models.Model):
    # Define fields
    name = models.CharField(max_length=100)
    hint = models.TextField()

    def __str__(self):
        return self.name