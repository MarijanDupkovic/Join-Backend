# Generated by Django 4.2.5 on 2023-09-16 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('color_key', models.CharField(max_length=20, verbose_name='Hex Color Key')),
                ('created_at', models.DateField(default=datetime.date.today, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(default=None, max_length=70, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('created_at', models.DateField(default=datetime.date.today, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name='Description')),
                ('prio', models.IntegerField()),
                ('assigned_users', models.JSONField(blank=True, null=True, verbose_name='Assigned to')),
                ('created_at', models.DateField(default=datetime.date.today, verbose_name='Created At')),
                ('due_date', models.DateField(default=datetime.date.today, verbose_name='Due Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='tasks.categoryitem')),
            ],
        ),
    ]
