# Generated by Django 3.1.6 on 2021-02-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_remove_property_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
