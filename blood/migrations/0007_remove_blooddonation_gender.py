# Generated by Django 4.2 on 2024-12-05 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_blooddonation_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonation',
            name='gender',
        ),
    ]
