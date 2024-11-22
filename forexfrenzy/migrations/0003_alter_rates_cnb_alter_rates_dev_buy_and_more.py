# Generated by Django 5.1.3 on 2024-11-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forexfrenzy', '0002_flags_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='cnb',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='dev_buy',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='dev_mid',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='dev_sale',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='vault_buy',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='vault_mid',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='vault_sale',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
