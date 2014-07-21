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
            field=models.DateTimeField(verbose_name='modified', default=datetime.datetime(2014, 7, 20, 20, 11, 52, 269558)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(verbose_name='created', default=datetime.datetime(2014, 7, 20, 20, 11, 52, 269610)),
            preserve_default=True,
        ),
    ]
