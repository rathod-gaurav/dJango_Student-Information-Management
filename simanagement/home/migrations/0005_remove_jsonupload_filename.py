# Generated by Django 4.0.5 on 2022-06-14 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_jsonupload_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsonupload',
            name='filename',
        ),
    ]