from rest_framework import serializers
import base64
import webcolors
from django.core.files.base import ContentFile

import datetime as dt

from .models import Whore, Achievement, AchievementWhore


class Hex2NameColor(serializers.Field):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class WhoreSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)
    age = serializers.SerializerMethodField()
    panty_color = Hex2NameColor()
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Whore
        fields = ('id', 'name', 'panty_color', 'venereal', 'birth_year',
                  'boobs', 'feature', 'owner', 'age', 'achievements', 'image')
        read_only_fields = ('owner',)

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        if 'achievements' not in self.initial_data:
            whore = Whore.objects.create(**validated_data)
            return whore
        else:
            achievements = validated_data.pop('achievements')
            whore = Whore.objects.create(**validated_data)
            for achievement in achievements:
                current_achievement, status = Achievement.objects.get_or_create(**achievement)
            AchievementWhore.objects.create(
                achievement=current_achievement, whore=whore)
            return whore

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('panty_color', instance.panty_color)
        instance.birth_year = validated_data.get(
            'birth_year', instance.birth_year
            )
        instance.image = validated_data.get('image', instance.image)
        if 'achievements' in validated_data:
            achievements_data = validated_data.pop('achievements')
            lst = []
            for achievement in achievements_data:
                current_achievement, status = Achievement.objects.get_or_create(
                    **achievement
                    )
                lst.append(current_achievement)
            instance.achievements.set(lst)

        instance.save()
        return instance
