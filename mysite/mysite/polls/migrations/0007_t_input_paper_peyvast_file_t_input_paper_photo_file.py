# Generated by Django 4.1.5 on 2023-02-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_t_user_erja'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_input_paper',
            name='peyvast_file',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='t_input_paper',
            name='photo_file',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]