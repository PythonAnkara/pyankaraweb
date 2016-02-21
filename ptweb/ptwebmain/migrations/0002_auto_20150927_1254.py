# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ptwebmain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
        'Post', 'categories_id', 'category_id'
    )
    ]
