# Generated by Django 4.2.6 on 2023-10-30 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_plantationproduct_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0003_alter_plantationrentalmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantationrentalmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.plantationproduct'),
        ),
        migrations.AlterField(
            model_name='plantationrentalmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL),
        ),
    ]