# Generated by Django 3.0.6 on 2020-05-30 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200530_2246'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vector',
            unique_together={('sip', 'dip')},
        ),
    ]
