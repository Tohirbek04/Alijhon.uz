# Generated by Django 5.0.6 on 2024-06-21 11:18

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('summa', models.FloatField(db_default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('chek', models.ImageField(upload_to='users/transaction')),
            ],
        ),
    ]
