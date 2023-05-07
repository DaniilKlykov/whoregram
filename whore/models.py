from django.db import models


class Whore(models.Model):
    class Meta:
        db_table = 'whore'

    name = models.CharField(max_length=15)
    venereal = models.CharField(max_length=20, null=True)
    birth_year = models.IntegerField()
    boobs = models.IntegerField()
    feature = models.CharField(max_length=20, null=True)    # особенность (её фишка)

    def __str__(self):
        return f'{self.name}, {self.venereal}, {self.boobs}'
