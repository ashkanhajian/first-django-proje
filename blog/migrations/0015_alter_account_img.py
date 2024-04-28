# Generated by Django 5.0.3 on 2024-04-28 22:37

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_account_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=90, scale=None, size=[500, 500], upload_to='account_images/'),
        ),
    ]
