# Generated by Django 5.0.6 on 2024-05-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='abilities',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='defense',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='special_attack',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='special_defense',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='type1',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='type2',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
