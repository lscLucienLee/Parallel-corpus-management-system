# Generated by Django 4.2 on 2023-05-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpusInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='用户名')),
                ('name', models.CharField(max_length=20, verbose_name='语料库名')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
            ],
        ),
        migrations.DeleteModel(
            name='Chy',
        ),
    ]
