# Generated by Django 3.1.6 on 2021-03-01 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('property', '0006_property_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='images.imagealbum'),
        ),
    ]
