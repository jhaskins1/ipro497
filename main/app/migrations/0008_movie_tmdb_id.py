# Generated by Django 4.1.2 on 2022-11-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cast_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
