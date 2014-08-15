# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_published_created_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created', editable=False),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='modified', editable=False),
        ),
    ]
