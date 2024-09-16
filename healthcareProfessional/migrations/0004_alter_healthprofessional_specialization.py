# Generated by Django 5.1.1 on 2024-09-15 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareProfessional', '0003_healthprofessional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthprofessional',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='healthcareProfessional.specialization'),
        ),
    ]
