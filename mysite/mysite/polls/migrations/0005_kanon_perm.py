# Generated by Django 4.1.5 on 2023-02-06 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_login_kanon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kanon_perm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('show_step', 'namayesh step mahramenh'), ('show_base_seting', 'namayesh tanzimat avaliyeh')),
            },
        ),
    ]