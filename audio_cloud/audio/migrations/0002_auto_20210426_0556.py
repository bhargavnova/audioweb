# Generated by Django 3.2 on 2021-04-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]