# Generated by Django 5.0.6 on 2024-06-28 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_reportproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_working_time', models.TimeField(verbose_name='operator ishga kelish vaqati')),
                ('to_working_time', models.TimeField(verbose_name='operator ishdan ketish vaqti')),
                ('passport', models.CharField(max_length=9)),
                ('operator', models.OneToOneField(limit_choices_to={'type': 'operator'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
