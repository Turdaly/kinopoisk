# Generated by Django 4.1.7 on 2023-05-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0015_alter_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]