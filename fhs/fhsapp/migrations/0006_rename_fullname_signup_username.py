# Generated by Django 4.1.7 on 2023-04-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fhsapp', '0005_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='fullname',
            new_name='username',
        ),
    ]
