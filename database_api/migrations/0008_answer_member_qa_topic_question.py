# Generated by Django 3.2.9 on 2022-02-12 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_api', '0007_alter_race_answer_race_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='QA_Topic',
            fields=[
                ('QA_id', models.AutoField(primary_key=True, serialize=False)),
                ('QA_doc', models.TextField(max_length=255)),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_api.course')),
            ],
            options={
                'db_table': 'qa_topic',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('Q_id', models.AutoField(primary_key=True, serialize=False)),
                ('Q_doc', models.TextField(max_length=255)),
                ('QA_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_api.qa_topic')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Answer_Member',
            fields=[
                ('Answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('Answer_doc', models.TextField(max_length=255)),
                ('Answer', models.BooleanField(default=True)),
                ('Q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_api.question')),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_api.student')),
            ],
            options={
                'db_table': 'answer_member',
            },
        ),
    ]
