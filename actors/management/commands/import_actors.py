import csv
from django.core.management.base import BaseCommand
from datetime import datetime

from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do Arquivo com Atores'
        )

    
    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Gravando Ator: {name}'))

                Actor.objects.create(


                   name=name,
                   birthday = birthday,
                   nationality = nationality, 
                )

        self.stdout.write(self.style.SUCCESS('Atores Importados com Sucesso!'))
