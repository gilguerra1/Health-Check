# Generated by Django 5.1.1 on 2024-10-02 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareProfessional', '0003_healthprofessional_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthprofessional',
            name='user',
        ),
    ]
