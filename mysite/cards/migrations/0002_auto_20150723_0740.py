# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_field', models.URLField()),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to=b'uploads')),
                ('media_type', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(verbose_name=b'created at')),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
