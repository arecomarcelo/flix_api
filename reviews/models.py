from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.PROTECT,
                              related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação Negativa não é Permitida!'),
            MaxValueValidator(5, 'Avaliação acima de 5 não é Permitida!')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['movie']
        verbose_name = 'Avaliaçõe'

    def __str__(self):
        return str(self.movie)
