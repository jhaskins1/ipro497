# Generated by Django 4.1.2 on 2022-11-20 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_movie_runtime_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime_length',
            field=models.DurationField(),
        ),
    ]
