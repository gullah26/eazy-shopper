# Generated by Django 4.1 on 2022-08-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('date', models.EmailField(max_length=25)),
                ('entry', models.CharField(max_length=1000)),
            ],
        ),
    ]
