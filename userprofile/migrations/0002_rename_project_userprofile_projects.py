# Generated by Django 4.2.11 on 2024-03-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='project',
            new_name='projects',
        ),
    ]
