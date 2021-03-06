# Generated by Django 3.1.1 on 2020-10-13 05:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('categoría', models.CharField(blank=True, max_length=50, null=True)),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(default='Producto', max_length=50)),
                ('cantidad', models.IntegerField(default='0')),
                ('código', models.CharField(max_length=13, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,13}$')])),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
    ]
