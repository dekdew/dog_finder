# Generated by Django 2.1.7 on 2019-05-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190506_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='dog',
        ),
    ]
