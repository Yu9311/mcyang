# Generated by Django 3.2.9 on 2022-02-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_api', '0002_alter_teacher_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='S_Email',
            field=models.TextField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='T_Email',
            field=models.TextField(max_length=50, unique=True),
        ),
    ]
