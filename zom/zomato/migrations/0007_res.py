# Generated by Django 2.2.5 on 2019-09-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0006_cities_entity'),
    ]

    operations = [
        migrations.CreateModel(
            name='res',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('img', models.ImageField(upload_to='pics')),
                ('url', models.URLField(max_length=50)),
            ],
        ),
    ]
