# Generated by Django 4.2.8 on 2024-05-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0005_rename_fin_co_no_depositoptions06_fin_prdt_cd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositcart',
            name='product',
        ),
        migrations.AddField(
            model_name='depositcart',
            name='product',
            field=models.ManyToManyField(to='deposits.depositproducts'),
        ),
    ]
