# Generated by Django 5.0.6 on 2024-06-27 21:11

import users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportProxy',
            fields=[
            ],
            options={
                'verbose_name': 'User balance report',
                'verbose_name_plural': 'User balance reports',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.UserModelManager()),
            ],
        ),
    ]