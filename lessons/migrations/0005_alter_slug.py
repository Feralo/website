# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_add_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='peter', max_length=40, editable=False),
        ),
    ]
