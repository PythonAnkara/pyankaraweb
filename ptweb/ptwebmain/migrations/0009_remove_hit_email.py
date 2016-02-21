# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptwebmain', '0008_auto_20151215_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hit',
            name='email',
        ),
    ]
