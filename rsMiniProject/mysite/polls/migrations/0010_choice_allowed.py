# Generated by Django 3.0.8 on 2020-07-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200726_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='allowed',
            field=models.BooleanField(default=True),
        ),
    ]
