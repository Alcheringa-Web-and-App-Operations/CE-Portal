# Generated by Django 4.1.2 on 2022-11-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0012_city_comingsoon'),
        ('users', '0021_remove_person_competition_person_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='competition',
        ),
        migrations.AddField(
            model_name='person',
            name='competition',
            field=models.ManyToManyField(blank=True, null=True, to='city.competition'),
        ),
    ]
