# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_nazarkov', '0009_auto_20150425_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='ask_nazarkov.UserProfile'),
            preserve_default=True,
        ),
    ]
