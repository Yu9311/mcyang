# Generated by Django 3.2.9 on 2022-02-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_api', '0009_auto_20220212_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Group_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team_desc',
            name='Group_Total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team_desc',
            name='Group_limit',
            field=models.IntegerField(),
        ),
    ]
