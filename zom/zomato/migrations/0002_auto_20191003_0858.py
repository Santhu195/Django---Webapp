# Generated by Django 2.2.4 on 2019-10-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rst',
            name='adress',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rst',
            name='url',
            field=models.URLField(),
        ),
    ]
