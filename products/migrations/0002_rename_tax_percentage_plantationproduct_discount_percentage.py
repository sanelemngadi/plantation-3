# Generated by Django 4.2.6 on 2023-10-28 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantationproduct',
            old_name='tax_percentage',
            new_name='discount_percentage',
        ),
    ]
