# Generated by Django 3.1.6 on 2021-03-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagealbum',
            name='name',
            field=models.CharField(default='UnknownAlbum', max_length=255),
        ),
    ]
