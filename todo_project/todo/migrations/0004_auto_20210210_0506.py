# Generated by Django 3.1 on 2021-02-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201123_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_images/def.png', upload_to='profile_images', verbose_name='Profile image'),
        ),
    ]
