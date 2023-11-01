# Generated by Django 4.2.6 on 2023-10-28 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_plantationnotificationstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantationNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='plantationnotificationsmodel',
            name='event',
        ),
        migrations.RemoveField(
            model_name='plantationnotificationsmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='plantationnotificationstatus',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='plantationnotificationstatus',
            name='read',
        ),
        migrations.RemoveField(
            model_name='plantationnotificationstatus',
            name='user',
        ),
        migrations.AddField(
            model_name='plantationnotificationstatus',
            name='message',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantationnotificationstatus',
            name='notification_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PlantationMessageNotification',
        ),
        migrations.DeleteModel(
            name='PlantationNotificationsModel',
        ),
        migrations.AddField(
            model_name='plantationnotification',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.plantationnotificationstatus'),
        ),
        migrations.AddField(
            model_name='plantationnotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]