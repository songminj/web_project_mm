# Generated by Django 4.2.8 on 2024-05-18 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_author_article_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='board',
            new_name='article',
        ),
    ]