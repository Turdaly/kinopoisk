# Generated by Django 4.1.6 on 2023-02-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('manufacturing_date', models.DateField()),
            ],
        ),
    ]
