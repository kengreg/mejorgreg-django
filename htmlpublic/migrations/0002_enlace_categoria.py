# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlpublic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='categoria',
            field=models.ForeignKey(to='htmlpublic.Categoria', default=0),
            preserve_default=False,
        ),
    ]
