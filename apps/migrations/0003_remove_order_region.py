# Generated by Django 5.0.6 on 2024-07-06 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='region',
        ),
    ]
