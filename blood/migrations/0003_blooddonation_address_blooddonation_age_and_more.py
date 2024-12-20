# Generated by Django 4.2 on 2024-12-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_alter_blooddonation_options_blooddonation_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonation',
            name='address',
            field=models.TextField(default='No address provided'),
        ),
        migrations.AddField(
            model_name='blooddonation',
            name='age',
            field=models.IntegerField(default='20', max_length=2),
        ),
        migrations.AddField(
            model_name='blooddonation',
            name='gender',
            field=models.CharField(default='male', max_length=10),
        ),
    ]
