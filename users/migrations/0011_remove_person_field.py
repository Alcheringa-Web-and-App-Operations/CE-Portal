# Generated by Django 4.0.5 on 2022-09-28 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_person_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='field',
        ),
    ]