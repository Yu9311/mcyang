# Generated by Django 3.2.9 on 2022-02-12 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_api', '0008_answer_member_qa_topic_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Group_number',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team_desc',
            name='Group_Total',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team_desc',
            name='Group_limit',
            field=models.IntegerField(max_length=50),
        ),
    ]
