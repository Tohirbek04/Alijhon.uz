# Generated by Django 5.0.6 on 2024-06-28 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0049_alter_missedcallorderproxymodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
