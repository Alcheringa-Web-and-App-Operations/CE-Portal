# Generated by Django 4.0.4 on 2022-09-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('users', '0002_team_competition_remove_person_competition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='city.city'),
        ),
    ]
