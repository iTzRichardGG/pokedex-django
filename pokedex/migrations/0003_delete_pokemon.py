# Generated by Django 5.0.6 on 2024-05-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_rename_abilities_pokemon_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pokemon',
        ),
    ]