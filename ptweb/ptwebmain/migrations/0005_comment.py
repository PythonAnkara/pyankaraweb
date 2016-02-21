# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptwebmain', '0004_auto_20151212_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('ipaddress', models.GenericIPAddressField(protocol='IPv4')),
                ('message', models.TextField(max_length=10000)),
                ('pub_datetime', models.DateTimeField(auto_now=True)),
                ('parentid', models.IntegerField()),
                ('post', models.ForeignKey(to='ptwebmain.Post')),
            ],
        ),
    ]
