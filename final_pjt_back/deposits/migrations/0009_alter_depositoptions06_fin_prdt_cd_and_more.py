# Generated by Django 4.2.8 on 2024-05-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0008_remove_depositproducts_like_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoptions06',
            name='fin_prdt_cd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='depositoptions12',
            name='fin_prdt_cd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='depositoptions24',
            name='fin_prdt_cd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='depositoptions36',
            name='fin_prdt_cd',
            field=models.TextField(),
        ),
    ]
