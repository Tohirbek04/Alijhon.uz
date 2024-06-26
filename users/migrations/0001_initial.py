# Generated by Django 5.0.6 on 2024-06-09 10:52

import django.utils.timezone
from django.db import migrations, models

import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this auth has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the auth can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this auth should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.CharField(choices=[('operator', 'Operator'), ('manager', 'Manager'), ('admin', 'Admin'), ('client', 'Client')], default='client', max_length=10)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this auth belongs to. A auth will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='auth', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this auth.', related_name='user_set', related_query_name='auth', to='auth.permission', verbose_name='auth permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.UserModelManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.AdminProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClientProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.ClientProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='ManagerProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.ManagerProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='OperatorProxyModel',
            fields=[
            ],
            options={
                'verbose_name': 'Operator',
                'verbose_name_plural': 'Operators',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.OperatorProxyManager()),
            ],
        ),
    ]
