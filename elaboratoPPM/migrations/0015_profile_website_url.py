# Generated by Django 5.0.6 on 2024-06-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elaboratoPPM', '0014_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
