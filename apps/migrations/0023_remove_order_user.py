# Generated by Django 5.0.6 on 2024-06-19 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
