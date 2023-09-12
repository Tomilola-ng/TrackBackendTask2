from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} person"
