# Generated by Django 2.2.5 on 2019-09-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0003_auto_20190928_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
