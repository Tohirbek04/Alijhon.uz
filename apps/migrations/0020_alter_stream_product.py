# Generated by Django 5.0.6 on 2024-06-18 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0019_delete_visitorderproxymodel_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='apps.product'),
        ),
    ]