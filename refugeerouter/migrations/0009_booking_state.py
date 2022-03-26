# Generated by Django 4.0.2 on 2022-03-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugeerouter', '0008_delete_notifier_remove_trip_driver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='state',
            field=models.CharField(choices=[('C', 'Closed'), ('F', 'Confirmed'), ('D', 'Denied'), ('I', 'Inhabited'), ('O', 'Open'), ('R', 'Requested')], default='O', max_length=1),
        ),
    ]
