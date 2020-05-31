# Generated by Django 3.0.6 on 2020-05-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200530_2329'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vector',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='Ip address')),
                ('outdegree', models.IntegerField(null=True, verbose_name='Semi-degree of outcome')),
                ('indegree', models.IntegerField(null=True, verbose_name='Half degree of approach')),
                ('outgoing_weight', models.IntegerField(null=True, verbose_name='')),
                ('incoming_weight', models.IntegerField(null=True, verbose_name='')),
                ('degree_centrality', models.IntegerField(null=True, verbose_name='')),
            ],
            options={
                'unique_together': {('ip',)},
            },
        ),
        migrations.RemoveField(
            model_name='vector',
            name='dip',
        ),
        migrations.RemoveField(
            model_name='vector',
            name='sip',
        ),
    ]
