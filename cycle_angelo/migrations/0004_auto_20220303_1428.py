# Generated by Django 2.2.26 on 2022-03-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_angelo', '0003_auto_20220303_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
