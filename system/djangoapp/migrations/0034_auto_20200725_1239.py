# Generated by Django 2.1 on 2020-07-25 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0033_auto_20200725_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
