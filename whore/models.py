from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Owner(models.Model):
    nickname = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nickname} {self.first_name}'


class Whore(models.Model):
    class Meta:
        db_table = 'whore'

    name = models.CharField(max_length=15)
    venereal = models.CharField(max_length=20, null=True)
    birth_year = models.IntegerField()
    boobs = models.IntegerField()
    feature = models.CharField(max_length=20, null=True)  # (её фишка)
    owner = models.ForeignKey(
        Owner, related_name='whore', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement,
                                          through='AchievementWhore')

    def __str__(self):
        return self.name


class AchievementWhore(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    whore = models.ForeignKey(Whore, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.whore}'
