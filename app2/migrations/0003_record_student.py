# Generated by Django 4.1.1 on 2022-09-23 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_muallif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=50)),
                ('kitob', models.CharField(max_length=50)),
                ('olingan_sana', models.DateField()),
                ('qaytardi', models.BooleanField()),
                ('qaytargan_sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('guruh', models.CharField(max_length=50)),
                ('kitob_soni', models.PositiveSmallIntegerField()),
                ('bitiruvchi', models.BooleanField()),
            ],
        ),
    ]