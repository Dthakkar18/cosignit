# Generated by Django 4.2.1 on 2023-07-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=225)),
                ('lastName', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('birthday', models.DateField()),
            ],
        ),
    ]
