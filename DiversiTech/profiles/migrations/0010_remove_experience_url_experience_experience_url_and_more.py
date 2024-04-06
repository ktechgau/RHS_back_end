# Generated by Django 5.0.3 on 2024-04-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_profile_area_profile_country_profile_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='url',
        ),
        migrations.AddField(
            model_name='experience',
            name='experience_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='picture_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
