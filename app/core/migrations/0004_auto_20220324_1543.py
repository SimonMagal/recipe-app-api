# Generated by Django 2.1.15 on 2022-03-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingrediens'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingrediens',
            new_name='Ingredient',
        ),
    ]
