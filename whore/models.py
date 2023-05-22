from django.db import models
from django.contrib.auth import get_user_model


CHOICES = (
    ('Gray', 'Серый'),
    ('Black', 'Черный'),
    ('White', 'Белый'),
    ('Ginger', 'Рыжий'),
    ('Mixed', 'Смешанный'),
)

User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Whore(models.Model):
    name = models.CharField(max_length=15)
    panty_color = models.CharField(max_length=15, null=True)
    venereal = models.CharField(max_length=20, null=True)
    birth_year = models.IntegerField()
    boobs = models.IntegerField()
    feature = models.CharField(max_length=20, null=True)  # (её фишка)
    owner = models.ForeignKey(
        User, related_name='whores', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement,
                                          through='AchievementWhore')
    image = models.ImageField(
        upload_to='whore/images/',
        null=True,
        default=None
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owner'],
                name='unique_name_owner'
            )
        ]

    def __str__(self):
        return self.name


class AchievementWhore(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    whore = models.ForeignKey(Whore, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.whore}'
