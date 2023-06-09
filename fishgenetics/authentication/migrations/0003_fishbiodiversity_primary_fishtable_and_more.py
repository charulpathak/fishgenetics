# Generated by Django 4.1.6 on 2023-03-28 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_habitatparameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='fishbiodiversity_primary',
            fields=[
                ('siteid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_river', models.CharField(max_length=200)),
                ('name_of_sampling_site', models.CharField(max_length=200)),
                ('date_of_collection', models.DateField()),
                ('collection_source', models.CharField(max_length=200)),
                ('sampling_area', models.IntegerField()),
                ('duration_of_fishing', models.DateTimeField()),
                ('time_of_fishing', models.DateTimeField()),
                ('total_catch', models.IntegerField()),
                ('number_of_species', models.IntegerField()),
                ('riverid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.form')),
            ],
        ),
        migrations.CreateModel(
            name='fishtable',
            fields=[
                ('fishid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_fish', models.CharField(max_length=200)),
                ('local_name', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('total_number', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('proportion_to_catch', models.IntegerField()),
                ('gear_used', models.IntegerField()),
                ('siteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.fishbiodiversity_primary')),
            ],
        ),
        migrations.CreateModel(
            name='fishbioforexoticfish',
            fields=[
                ('afishid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_fish_genus_and_species', models.CharField(max_length=200)),
                ('local_name', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('total_number', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('proportion_to_catch', models.IntegerField()),
                ('gear_used', models.IntegerField()),
                ('siteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.fishbiodiversity_primary')),
            ],
        ),
        migrations.CreateModel(
            name='fishbiodiversitysec',
            fields=[
                ('riverid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_fish', models.CharField(max_length=200)),
                ('largest_size', models.IntegerField()),
                ('breeding_information', models.CharField(max_length=200)),
                ('known_economic', models.IntegerField()),
                ('local_name', models.CharField(max_length=200)),
                ('commercial_value', models.CharField(max_length=200)),
                ('siteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.fishbiodiversity_primary')),
            ],
        ),
    ]
