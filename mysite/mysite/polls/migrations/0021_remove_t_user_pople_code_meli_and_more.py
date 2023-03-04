# Generated by Django 4.1.5 on 2023-02-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_rename_photo_dsign_t_sign_digital_photo_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_user_pople',
            name='code_meli',
        ),
        migrations.RemoveField(
            model_name='t_user_pople',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='t_user_pople',
            name='permination_id',
        ),
        migrations.AddField(
            model_name='t_user_pople',
            name='linker',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='t_user_pople',
            name='organ',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='t_user_pople',
            name='tozih',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='t_user_pople',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='t_user_pople',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
