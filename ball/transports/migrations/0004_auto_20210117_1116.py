# Generated by Django 3.1.5 on 2021-01-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0003_auto_20210117_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportfieldsmodel',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transports.countrymodel'),
        ),
    ]
