# Generated by Django 3.1.5 on 2021-01-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210112_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]