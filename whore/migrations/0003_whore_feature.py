# Generated by Django 3.2 on 2023-05-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whore', '0002_alter_whore_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='whore',
            name='feature',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
