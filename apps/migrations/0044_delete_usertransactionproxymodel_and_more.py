# Generated by Django 5.0.6 on 2024-06-24 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0043_operatortransactionproxymodel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTransactionProxyModel',
        ),
        migrations.CreateModel(
            name='ClientTransactionProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Transaction Client',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.transaction',),
        ),
    ]
