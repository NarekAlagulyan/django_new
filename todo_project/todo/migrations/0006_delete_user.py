# Generated by Django 3.1 on 2021-02-10 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210210_0532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]