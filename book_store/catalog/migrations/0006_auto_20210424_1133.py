# Generated by Django 3.1.7 on 2021-04-24 07:03

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_delete_bookcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_publish',
            field=django_jalali.db.models.jDateField(),
        ),
    ]