# Generated by Django 5.1 on 2024-09-10 00:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliação Negativa não é Permitida!'), django.core.validators.MaxValueValidator(5, 'Avaliação acima de 5 não é Permitida!')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movies.movie')),
            ],
            options={
                'verbose_name': 'Review',
                'ordering': ['movie'],
            },
        ),
    ]
