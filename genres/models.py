from django.db import models

class Genre (models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Gênero'
    
    def __str__(self):
        return self.name