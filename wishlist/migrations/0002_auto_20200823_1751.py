# Generated by Django 3.1 on 2020-08-23 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movie_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wishlist.movies'),
        ),
    ]
