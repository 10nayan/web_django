# Generated by Django 3.0.7 on 2020-06-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0006_auto_20200627_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(),
        ),
    ]