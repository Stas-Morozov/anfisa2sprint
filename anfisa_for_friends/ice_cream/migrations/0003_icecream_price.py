# Generated by Django 3.2.16 on 2024-01-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240127_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
