# Generated by Django 5.1.6 on 2025-02-15 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_rename_consultation_consultations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultations',
            old_name='geral_registration',
            new_name='general_registration',
        ),
    ]
