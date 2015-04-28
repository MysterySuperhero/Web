# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_nazarkov', '0006_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(to='ask_nazarkov.UserProfile'),
            preserve_default=True,
        ),
    ]
