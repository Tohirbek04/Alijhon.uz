# Generated by Django 5.0.6 on 2024-06-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0035_alter_competition_end_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
    ]