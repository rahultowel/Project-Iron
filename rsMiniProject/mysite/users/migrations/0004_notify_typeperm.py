# Generated by Django 3.0.8 on 2020-07-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_polluser_nots'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='typePerm',
            field=models.BooleanField(default=False),
        ),
    ]
