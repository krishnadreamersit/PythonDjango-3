# Generated by Django 4.0.1 on 2022-01-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('caddress', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_person',
            },
        ),
    ]
