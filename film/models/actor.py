from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    birthdate = models.DateField(blank=True, null=True)
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)

    def __str__(self):
        return self.name
