# Generated by Django 2.2 on 2021-08-06 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='file',
            new_name='summery_file',
        ),
        migrations.RemoveField(
            model_name='book',
            name='type',
        ),
    ]