# Generated by Django 4.0.5 on 2022-09-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_remove_position_left_remove_position_top_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='background_img',
            field=models.ImageField(default='dcity.jpg', upload_to='competition_background_images'),
        ),
    ]
