# Generated by Django 5.0.6 on 2024-06-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elaboratoPPM', '0020_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='città',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='età',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
