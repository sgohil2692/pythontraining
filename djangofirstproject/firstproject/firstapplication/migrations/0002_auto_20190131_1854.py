# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(unique=True, max_length=20)),
                ('last_name', models.CharField(unique=True, max_length=20)),
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topics',
            field=models.ForeignKey(to='firstapplication.Person'),
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
