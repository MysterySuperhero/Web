# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('ask_nazarkov', '0004_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
