# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 11, 16, 9, 59, 731900), verbose_name='modified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 11, 16, 9, 59, 731945), verbose_name='created'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
