# Generated by Django 4.2.8 on 2024-05-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0009_alter_depositoptions06_fin_prdt_cd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoptions06',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions06',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions12',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions12',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions24',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions24',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions36',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions36',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
    ]
