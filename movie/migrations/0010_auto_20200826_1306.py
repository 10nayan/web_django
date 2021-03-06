# Generated by Django 3.0.7 on 2020-08-26 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_remove_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Disliked_movies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliked_movies', to='movie.Movies'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Liked_movies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_movies', to='movie.Movies'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Watch_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to='movie.Movies'),
        ),
    ]
