from django.db import models

from core.managers import VectorModelManager, FrameModelManager


class Frame(models.Model):
    length = models.IntegerField(verbose_name='Length')
    destination = models.GenericIPAddressField(verbose_name='Destination')
    source = models.GenericIPAddressField(verbose_name='Source')
    
    objects = FrameModelManager()
    
    def __str__(self):
        return f'<Frame from {self.source} to {self.destination}, {self.length}>'


# noinspection SpellCheckingInspection
class Vector(models.Model):
    sip = models.ForeignKey('Node', on_delete=models.CASCADE, verbose_name='Source host', related_name='vector_sip')
    dip = models.ForeignKey('Node', on_delete=models.CASCADE, verbose_name='Destination host', related_name='vector_dip') # noqa
    srcpkts = models.IntegerField(verbose_name='Count frames from sip -> dip')
    drcpkts = models.IntegerField(verbose_name='Count frames from dip -> sip')
    
    objects = VectorModelManager()
    
    class Meta:
        unique_together = ("sip", "dip")


# noinspection SpellCheckingInspection
class Node(models.Model):
    ip = models.GenericIPAddressField(verbose_name='Ip address')
    outdegree = models.IntegerField(verbose_name='Semi-degree of outcome', null=True)
    indegree = models.IntegerField(verbose_name='Half degree of approach', null=True)
    outgoing_weight = models.IntegerField(verbose_name='', null=True)
    incoming_weight = models.IntegerField(verbose_name='', null=True)
    degree_centrality = models.IntegerField(verbose_name='', null=True)
    
    objects = models.Manager()
    
    class Meta:
        unique_together = ("ip", )
