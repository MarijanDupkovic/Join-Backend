# Generated by Django 4.2.5 on 2023-09-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_taskitem_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='prio',
            field=models.IntegerField(default=0),
        ),
    ]
