# Generated by Django 3.2.7 on 2021-09-04 22:12

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('micro_tasks', '0003_auto_20210904_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default=0, max_length=2),
        ),
    ]