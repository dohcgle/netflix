from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    birthdate = models.DateField()
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.name
