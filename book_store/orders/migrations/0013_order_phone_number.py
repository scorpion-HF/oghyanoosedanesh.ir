# Generated by Django 3.2.4 on 2021-07-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20210626_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن'),
        ),
    ]
