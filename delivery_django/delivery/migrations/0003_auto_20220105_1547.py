# Generated by Django 3.2.11 on 2022-01-05 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20220105_1456'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='deliveryman',
            options={},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderform',
            options={},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={},
        ),
    ]