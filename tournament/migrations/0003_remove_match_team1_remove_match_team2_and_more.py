# Generated by Django 4.2.7 on 2023-11-02 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_teammatch_team1_teammatch_team2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='teammatch',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='teammatch',
            name='team2',
        ),
    ]