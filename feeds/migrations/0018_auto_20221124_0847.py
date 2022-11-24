# Generated by Django 3.2.16 on 2022-11-24 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0017_alter_personalinformation_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='github',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='link',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter',
        ),
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=150, null=True, verbose_name='full_name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='We will meet soon!', verbose_name='message'),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='contact',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='mayankdehariya200@gmail.com', max_length=100, verbose_name='email'),
        ),
    ]