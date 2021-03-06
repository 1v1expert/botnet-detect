# Generated by Django 3.0.6 on 2020-05-31 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200531_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='dip',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vector_dip', to='core.Node', verbose_name='Destination host'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vector',
            name='sip',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vector_sip', to='core.Node', verbose_name='Source host'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='vector',
            unique_together={('sip', 'dip')},
        ),
    ]
