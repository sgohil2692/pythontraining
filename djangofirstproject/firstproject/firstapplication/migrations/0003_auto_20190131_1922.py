# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapplication', '0002_auto_20190131_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('instrument', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topics',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='WebPage',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='firstapplication.Musician'),
        ),
    ]
