# Generated by Django 2.1 on 2020-07-29 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_auto_20200729_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='post',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
    ]
