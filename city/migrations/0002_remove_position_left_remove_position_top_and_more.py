# Generated by Django 4.0.4 on 2022-09-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='left',
        ),
        migrations.RemoveField(
            model_name='position',
            name='top',
        ),
        migrations.AddField(
            model_name='position',
            name='logoLeft',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='position',
            name='logoTop',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='position',
            name='textTop',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
