# Generated by Django 4.2.11 on 2024-03-18 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantproject', '0002_alter_plantproject_project_card_entries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantproject',
            name='project_card_entries',
        ),
        migrations.AddField(
            model_name='plantprojectcard',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_cards', to='plantproject.plantproject'),
            preserve_default=False,
        ),
    ]
