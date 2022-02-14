# Generated by Django 4.0.1 on 2022-02-13 09:03

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
                ('fullname', models.CharField(max_length=50)),
                ('contactaddress', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['pid', 'fullname', 'contactaddress'],
            },
        ),
    ]