# Generated by Django 4.2.8 on 2024-05-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositproducts',
            name='max_limit',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='depositproducts',
            name='mrtr_int',
            field=models.TextField(null=True),
        ),
    ]
