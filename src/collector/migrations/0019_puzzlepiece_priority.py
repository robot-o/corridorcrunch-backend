# Generated by Django 3.0.2 on 2020-01-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0018_confidentsolution_datahash'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzlepiece',
            name='priority',
            field=models.PositiveIntegerField(default=0, verbose_name='Priority value in transcription queue'),
        ),
    ]