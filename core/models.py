from django.db import models

from core.managers import FrameModelManager, VectorModelManager


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
        
    def __str__(self):
        return f'{self.dip} -{self.drcpkts}-> {self.sip} -{self.srcpkts}->{self.dip}'


# noinspection SpellCheckingInspection
class Node(models.Model):
    ip = models.GenericIPAddressField(verbose_name='Ip address')
    outdegree = models.IntegerField(verbose_name='Semi-degree of outcome', null=True)  # полустепень исхода
    indegree = models.IntegerField(verbose_name='Half degree of approach', null=True)  # полустепень захода
    outgoing_weight = models.IntegerField(verbose_name='Outgoing weight', null=True)  # вес исходящих
    incoming_weight = models.IntegerField(verbose_name='Incoming weight', null=True)  # вес входящих
    betweenness_centrality = models.FloatField(verbose_name='Betweenness centrality', null=True)  # степень посредничества, показывает, насколько узел связывает несколько несвязанных сообществ, или занимает позицию "между"  # noqa
    closeness_centrality = models.FloatField(verbose_name='Closeness centrality', null=True)  # показывает, насколько узел близок ко всем остальным узлам в сети  # noqa
    eigenvector_centrality = models.FloatField(verbose_name='Eigenvector centrality', null=True)  # показывает, насколько узел связан с узлами, которые сами имеют большое количество связей  # noqa
    clustering_coefficient = models.FloatField(verbose_name='Clustering coefficient', null=True)  # Локальный коэффициент кластеризации  # noqa
    alpha_centrality = models.FloatField(verbose_name='Alpha centrality', null=True)  # Мера центральных узлов в пределах графика   # noqa
    
    objects = models.Manager()
    
    class Meta:
        unique_together = ("ip", )
        
    def __str__(self):
        return f'<{self.ip}>'
