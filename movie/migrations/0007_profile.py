# Generated by Django 3.0.7 on 2020-08-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200731_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Liked_movies', models.TextField()),
                ('Disliked_movies', models.TextField()),
                ('Watch_list', models.TextField()),
            ],
        ),
    ]
