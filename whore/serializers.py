from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

import datetime as dt

from .models import Whore, User, Achievement, AchievementWhore, CHOICES


class UserSerializer(serializers.ModelSerializer):
    whore = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'first_name', 'whore')
        ref_name = 'ReadOnlyUsers'


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class WhoreSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)
    age = serializers.SerializerMethodField()
    panty_color = serializers.ChoiceField(choices=CHOICES)
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Whore
        fields = ('id', 'name', 'panty_color', 'venereal', 'birth_year',
                  'boobs', 'feature', 'owner', 'age', 'achievements')

        validators = [
            UniqueTogetherValidator(
                queryset=Whore.objects.all(),
                fields=('name', 'owner'),
                message='Такая сучка уже есть в нашей компании'
            )
        ]

    def validate_birth_year(self, value):
        year = dt.date.today().year
        if not (year - 55 < value <= year):
            raise serializers.ValidationError(
                'Старые шлюхи очень специфический товар, как и не родившиеся')
        return value

    def validate(self, data):
        if data['panty_color'] == data['name']:
            raise serializers.ValidationError(
                'Имя не может совпадать с цветом трусов')
        return data

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
                current_achievement,\
                    status = Achievement.objects.get_or_create(**achievement)
            AchievementWhore.objects.create(
                achievement=current_achievement, whore=whore)
            return whore
