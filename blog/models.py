

# Create your models here.
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

    def display_name_upper(self):
        return self.name.upper()

    display_name_upper.short_description = 'Name (Uppercase)'

    def __str__(self):
        return self.name



