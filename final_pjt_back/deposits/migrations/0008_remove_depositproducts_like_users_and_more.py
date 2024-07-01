# Generated by Django 4.2.8 on 2024-05-21 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0007_depositproducts_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositproducts',
            name='like_users',
        ),
        migrations.RemoveField(
            model_name='depositcart',
            name='product',
        ),
        migrations.AddField(
            model_name='depositcart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='deposits.depositproducts'),
            preserve_default=False,
        ),
    ]