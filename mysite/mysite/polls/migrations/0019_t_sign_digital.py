# Generated by Django 4.1.5 on 2023-02-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_t_input_paper_date_paper_see_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_sign_digital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_dsign', models.FileField(upload_to='')),
                ('user_sign_id', models.CharField(max_length=255)),
            ],
        ),
    ]