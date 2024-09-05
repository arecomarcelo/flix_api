from random import choices
from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, 
                                   choices=NATIONALITY_CHOICES,
                                   blank=True,
                                   null=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Atore'

    def __str__(self):
        return self.name