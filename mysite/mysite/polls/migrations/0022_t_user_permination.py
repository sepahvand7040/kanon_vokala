# Generated by Django 4.1.5 on 2023-02-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_remove_t_user_pople_code_meli_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_user_permination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.FileField(upload_to='')),
                ('user_perm', models.CharField(choices=[('1', 'عادی'), ('2', 'محرمانه'), ('3', 'فوق محرمانه')], max_length=1)),
            ],
        ),
    ]
