# Generated by Django 4.0.6 on 2022-10-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0011_city_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='comingsoon',
            field=models.BooleanField(default=False),
        ),
    ]
