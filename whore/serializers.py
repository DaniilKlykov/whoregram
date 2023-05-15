from rest_framework import serializers

from .models import Whore, Owner, Achievement, AchievementWhore


class OwnerSerializer(serializers.ModelSerializer):
    # whore = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = ('nickname', 'first_name', 'whore')


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')


class WhoreSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)

    class Meta:
        model = Whore
        fields = ('id', 'name', 'venereal', 'birth_year',
                  'boobs', 'feature', 'owner', 'achievements')

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
