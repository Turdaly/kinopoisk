# Generated by Django 4.1.6 on 2023-02-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0008_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='manufacturing_date',
            field=models.PositiveIntegerField(),
        ),
    ]
