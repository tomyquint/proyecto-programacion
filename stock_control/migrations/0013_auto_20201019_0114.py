# Generated by Django 3.1.1 on 2020-10-19 04:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_control', '0012_auto_20201019_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='código',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{13,13}$')]),
        ),
    ]
