# Generated by Django 2.0.5 on 2018-09-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
