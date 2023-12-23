# Generated by Django 5.0 on 2023-12-22 23:53

import django.db.models.functions.text
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Last Name')),
                ('full_name', models.GeneratedField(db_persist=True, expression=django.db.models.functions.text.Concat('first_name', models.Value(' '), 'last_name'), output_field=models.CharField(max_length=150, verbose_name='Full Name'))),
                ('nick_name', models.CharField(blank=True, max_length=40, verbose_name='Nick Name')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('about', models.TextField(blank=True, verbose_name='About')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
