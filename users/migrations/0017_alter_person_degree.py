# Generated by Django 4.0.5 on 2022-10-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_person_contactno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.TextField(blank=True, default='B.Tech', max_length=8, null=True),
        ),
    ]
