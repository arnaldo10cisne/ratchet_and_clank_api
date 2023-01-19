# Generated by Django 4.1.5 on 2023-01-19 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='first_appearance',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debuted', to='games.game'),
        ),
    ]
