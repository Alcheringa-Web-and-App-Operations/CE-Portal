# Generated by Django 4.1.1 on 2022-09-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_person_yearofgraduation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='college_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, default='B. Tech', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, default='Male', max_length=10, null=True),
        ),
    ]
