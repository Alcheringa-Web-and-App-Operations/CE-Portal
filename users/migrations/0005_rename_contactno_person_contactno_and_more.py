# Generated by Django 4.0.6 on 2022-09-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Contactno',
            new_name='contactno',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Email',
            new_name='email',
        ),
    ]
