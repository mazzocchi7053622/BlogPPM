# Generated by Django 5.0.6 on 2024-06-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elaboratoPPM', '0005_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
