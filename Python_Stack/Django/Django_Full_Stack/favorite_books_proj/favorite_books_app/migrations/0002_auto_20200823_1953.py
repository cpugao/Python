# Generated by Django 2.2.4 on 2020-08-24 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boook',
            new_name='Book',
        ),
    ]
