# Generated by Django 3.2.4 on 2021-06-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('studentid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=30, null=True, unique=True)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
