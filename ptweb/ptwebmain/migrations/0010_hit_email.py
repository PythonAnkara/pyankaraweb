# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptwebmain', '0009_remove_hit_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hit',
            name='email',
            field=models.CharField(default='#', max_length=255),
        ),
    ]
