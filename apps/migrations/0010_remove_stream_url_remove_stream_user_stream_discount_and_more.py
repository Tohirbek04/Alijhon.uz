# Generated by Django 5.0.6 on 2024-06-12 15:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_stream'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='url',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='user',
        ),
        migrations.AddField(
            model_name='stream',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stream',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stream',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='apps.product'),
        ),
    ]
