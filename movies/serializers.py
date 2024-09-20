from django.db.models import Avg
from rest_framework import serializers
from .models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None
    
        # reviews = obj.reviews.all()

        # if reviews:
        #     soma = 0

        #     for review in reviews:
        #         soma += review.stars

        #     contagem = reviews.count()
        #     media = soma / contagem

        #     return round(media,1)

        # return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A Data de Lançamento deve ser Superior a 1990")
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Descroção não pode Exceder 200 caracteres")
        return value