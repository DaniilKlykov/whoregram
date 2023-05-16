from rest_framework import serializers
import webcolors
import datetime as dt


from .models import Whore, Owner, Achievement, AchievementWhore, CHOICES


class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class OwnerSerializer(serializers.ModelSerializer):
    # whore = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = ('nickname', 'first_name', 'whore')


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class WhoreListSerializer(serializers.ModelSerializer):
    panty_color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Whore
        fields = ('id', 'name', 'panty_color')


class WhoreSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)
    age = serializers.SerializerMethodField()
    # panty_color = Hex2NameColor()
    panty_color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Whore
        fields = ('id', 'name', 'panty_color', 'venereal', 'birth_year',
                  'boobs', 'feature', 'owner', 'age', 'achievements')

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        if 'achievements' not in self.initial_data:
            whore = Whore.objects.create(**validated_data)
            return whore

        achievements = validated_data.pop('achievements')
        whore = Whore.objects.create(**validated_data)

        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            AchievementWhore.objects.create(
                achievement=current_achievement, whore=whore)
        return whore
