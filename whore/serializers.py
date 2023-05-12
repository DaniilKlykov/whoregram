from rest_framework import serializers

from .models import Whore


class WhoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whore
        fields = ('id', 'name', 'venereal', 'birth_year', 'boobs', 'feature')
