from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from film.models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, user_date):
        fix_date = datetime.strptime("1950-01-01", "%Y-%m-%d").date()
        if user_date < fix_date:
            raise ValidationError(detail='Kiritilgan sana 01.01.1950 yildan dan kichik')
        return user_date

