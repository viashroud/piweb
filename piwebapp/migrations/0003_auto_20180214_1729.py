# Generated by Django 2.0.2 on 2018-02-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piwebapp', '0002_remove_device_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('interface_type', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
