# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_add_created_and_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
