# Generated by Django 2.2.5 on 2019-09-28 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0002_auto_20190928_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='new_users',
            new_name='users',
        ),
    ]