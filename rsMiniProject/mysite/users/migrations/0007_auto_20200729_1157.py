# Generated by Django 3.0.8 on 2020-07-29 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200728_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify',
            old_name='not_from',
            new_name='not_memo',
        ),
    ]
