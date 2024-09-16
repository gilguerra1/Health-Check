# Generated by Django 5.1.1 on 2024-09-15 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareProfessional', '0004_alter_healthprofessional_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthprofessional',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='professional_specialization', to='healthcareProfessional.specialization'),
        ),
    ]
