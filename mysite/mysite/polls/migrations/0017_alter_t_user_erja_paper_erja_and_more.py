# Generated by Django 4.1.5 on 2023-02-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_remove_t_input_paper_photo_paper_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_user_erja',
            name='paper_erja',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='t_user_erja',
            name='user_deliver_erja',
            field=models.IntegerField(null=True),
        ),
    ]
