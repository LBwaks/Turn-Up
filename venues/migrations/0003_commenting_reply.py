# Generated by Django 3.2.4 on 2021-09-12 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_venue_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenting',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venue_replies', to='venues.commenting'),
        ),
    ]