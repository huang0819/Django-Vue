# Generated by Django 3.2.11 on 2022-01-05 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='deliveryman',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='orderform',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'managed': False},
        ),
    ]
