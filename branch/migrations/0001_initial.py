# Generated by Django 3.0.7 on 2020-06-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=250)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisarion',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=250)),
            ],
        ),
    ]
