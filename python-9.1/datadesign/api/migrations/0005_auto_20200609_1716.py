# Generated by Django 2.1.2 on 2020-06-09 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200609_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(8)]),
        ),
    ]
