# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_fix_date_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default=datetime.datetime.now, max_length=40),
            preserve_default=False,
        ),
    ]
