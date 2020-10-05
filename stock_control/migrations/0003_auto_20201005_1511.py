# Generated by Django 3.1.1 on 2020-10-05 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_control', '0002_auto_20201005_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='issue_quantity',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='category',
            new_name='categoría',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='created_by',
            new_name='código',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='issue_by',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='issue_to',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='receive_by',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='receive_quantity',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='reorder_level',
        ),
    ]