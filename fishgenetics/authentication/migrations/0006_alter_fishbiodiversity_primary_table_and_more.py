# Generated by Django 4.1.6 on 2023-04-06 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_fishbiodiversity_primary_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fishbiodiversity_primary',
            table='fishbiodiversity_primary',
        ),
        migrations.AlterModelTable(
            name='fishbiodiversitysec',
            table='fishbiodiversitysec',
        ),
        migrations.AlterModelTable(
            name='fishbioforexoticfish',
            table='fishbioforexoticfish',
        ),
        migrations.AlterModelTable(
            name='fishtable',
            table='fishtable',
        ),
        migrations.AlterModelTable(
            name='form',
            table='form',
        ),
        migrations.AlterModelTable(
            name='habitatparameter',
            table='habitatparameter',
        ),
    ]
