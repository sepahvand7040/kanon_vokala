# Generated by Django 4.1.5 on 2023-02-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_t_input_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_user_pople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('code_meli', models.CharField(max_length=255)),
                ('org_id', models.CharField(max_length=255)),
                ('permination_id', models.CharField(max_length=255)),
            ],
        ),
    ]