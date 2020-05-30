from django.db import models


class Frame(models.Model):
    length = models.IntegerField(verbose_name='Length')
    destination = models.GenericIPAddressField(verbose_name='Destination')
    source = models.GenericIPAddressField(verbose_name='Source')
    
    def __str__(self):
        return f'<Frame from {self.source} to {self.destination}, {self.length}>'


# noinspection SpellCheckingInspection
class Vector(models.Model):
    sip = models.GenericIPAddressField(verbose_name='Source host')
    dip = models.GenericIPAddressField(verbose_name='Destination host')
    srcpkts = models.IntegerField(verbose_name='Count frames from sip -> dip')
    drcpkts = models.IntegerField(verbose_name='Count frames from dip -> sip')
