# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(default='')),
                ('modified', models.DateTimeField(default=datetime.datetime(2014, 8, 8, 17, 38, 59, 484457), verbose_name='modified')),
                ('created', models.DateTimeField(default=datetime.datetime(2014, 8, 8, 17, 38, 59, 484500), verbose_name='created')),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
    ]
