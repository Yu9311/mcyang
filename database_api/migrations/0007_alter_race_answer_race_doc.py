# Generated by Django 3.2.9 on 2022-02-09 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_api', '0006_auto_20220208_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race_answer',
            name='Race_doc',
            field=models.TextField(max_length=255, unique=True),
        ),
    ]
