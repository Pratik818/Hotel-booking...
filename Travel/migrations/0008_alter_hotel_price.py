# Generated by Django 4.1.2 on 2023-03-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0007_hotel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.IntegerField(default=False),
        ),
    ]
