# Generated by Django 4.2 on 2023-05-16 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whore', '0006_whore_panty_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whore',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='whore',
            table=None,
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
