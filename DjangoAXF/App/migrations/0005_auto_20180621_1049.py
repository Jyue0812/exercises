# Generated by Django 2.0.5 on 2018-06-21 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_mainshow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainshow',
            old_name='childid1',
            new_name='childcid1',
        ),
        migrations.RenameField(
            model_name='mainshow',
            old_name='childid2',
            new_name='childcid2',
        ),
        migrations.RenameField(
            model_name='mainshow',
            old_name='childid3',
            new_name='childcid3',
        ),
    ]
