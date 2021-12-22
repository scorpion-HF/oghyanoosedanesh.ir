# Generated by Django 3.1.7 on 2021-06-17 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_comments_xtd', '0008_auto_20200920_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.xtdcomment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ('submit_date',),
                'permissions': [('can_moderate', 'Can moderate comments')],
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]