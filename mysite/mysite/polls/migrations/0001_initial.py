# Generated by Django 4.1.5 on 2023-01-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('joined_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='T_type_paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_paper', models.CharField(max_length=255)),
                ('code_paper', models.CharField(max_length=255)),
                ('sharh_paper', models.CharField(max_length=255)),
                ('pp_paper', models.CharField(max_length=255)),
            ],
        ),
    ]