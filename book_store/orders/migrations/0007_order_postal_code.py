# Generated by Django 3.1.7 on 2021-05-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.IntegerField(default=0),
        ),
    ]
