# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptwebmain', '0007_auto_20151214_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='hit',
            name='datatype',
            field=models.CharField(default='read', max_length=50),
        ),
        migrations.AddField(
            model_name='hit',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
