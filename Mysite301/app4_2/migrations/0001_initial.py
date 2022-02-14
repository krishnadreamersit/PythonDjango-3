# Generated by Django 4.0.1 on 2022-02-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('contact_address', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(blank=True, default='', max_length=50)),
                ('email', models.EmailField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]