# Generated by Django 4.1.5 on 2023-02-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_alter_t_user_permination_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_user_erja',
            name='tozih',
            field=models.TextField(null=True),
        ),
    ]
