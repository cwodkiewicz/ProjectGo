# Generated by Django 4.1.3 on 2022-11-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_type', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('destination_weather', models.IntegerField()),
            ],
        ),
    ]
