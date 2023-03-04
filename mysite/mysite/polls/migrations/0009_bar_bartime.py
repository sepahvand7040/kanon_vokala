# Generated by Django 4.1.5 on 2023-02-09 01:07

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_t_input_paper_peyvast_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', django_jalali.db.models.jDateField()),
            ],
        ),
        migrations.CreateModel(
            name='BarTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('datetime', django_jalali.db.models.jDateTimeField()),
            ],
        ),
    ]