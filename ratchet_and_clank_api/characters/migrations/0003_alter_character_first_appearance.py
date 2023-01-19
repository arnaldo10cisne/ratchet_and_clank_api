# Generated by Django 4.1.5 on 2023-01-19 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('characters', '0002_character_first_appearance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='first_appearance',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_debuted', to='games.game'),
        ),
    ]
