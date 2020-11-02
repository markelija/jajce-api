# Generated by Django 3.0.3 on 2020-11-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osnovnipodaci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Objekti u tvornici',
            },
        ),
        migrations.CreateModel(
            name='RadnaSmjena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Radne smjene',
            },
        ),
        migrations.CreateModel(
            name='VrstaOdrzavanja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Vrste održavanja',
            },
        ),
    ]
