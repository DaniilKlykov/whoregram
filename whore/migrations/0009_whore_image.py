# Generated by Django 3.2 on 2023-05-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whore', '0008_whore_unique_name_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='whore',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='whore/images/'),
        ),
    ]
