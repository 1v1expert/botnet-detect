import logging
from time import gmtime, strftime, time

import networkx as nx
from django.db.models import Q, Sum

from core.models import Frame, Node, Vector
from core.utils.network import DiGraph
from core.utils.pcap import PcapFileCapture

# Get an instance of a logger
in_logger = logging.getLogger('botnet')


class Preprocess:
    def __init__(self, logger=None):
        self.logger = logger or in_logger.info

    def frames_bulk_create(self, filename):
        self.logger('Start bulk frames create process')
    
        if Frame.objects.exists():
            self.logger(f'{Frame.objects.count()} frames has been deleted')
            Frame.objects.all().delete()

        # noinspection SpellCheckingInspection
        pcap_file = PcapFileCapture(filename=filename, limit=100000)
        frames: list = []
        for ic, frame in enumerate(pcap_file.read()):
            # pass
            self.logger(f'Frame {ic} -> {frame.as_dict()}')
            frames.append(Frame(**frame.as_dict()))
    
        Frame.objects.bulk_create(frames)
    
        self.logger(f'Time left: {strftime("%H:%M:%S", gmtime(time() - pcap_file.start_time))}')

    def vectors_bulk_create(self):
        self.logger('Start bulk vectors create process')
    
        start_time = time()
        if Vector.objects.exists():
            self.logger(f'{Vector.objects.count()} vectors has been deleted')
            Vector.objects.all().delete()
    
        frames = Frame.objects.distinct('source')
        frames_count = frames.count()
        for ic, frame in enumerate(frames):
            source, created = Node.objects.get_or_create(ip=frame.source)
            destination, created = Node.objects.get_or_create(ip=frame.destination)
        
            vectors = Vector.objects.filter(
                Q(sip=source, dip=destination) | Q(sip=destination, dip=source)
            )
            if vectors.exists():
                continue
        
            Vector.objects.create(
                sip=source,
                dip=destination,
                srcpkts=Frame.objects.filter(source=frame.source, destination=frame.destination).count(),
                drcpkts=Frame.objects.filter(source=frame.destination, destination=frame.source).count()
            )
        
            if ic % 50 == 0:
                self.logger(f'{ic} processed from {frames_count}')
    
        self.logger(f'Time left: {strftime("%H:%M:%S", gmtime(time() - start_time))}')

    # noinspection SpellCheckingInspection
    def upgrade_nodes(self):
        self.logger('Start upgrade nodes process')
        start_time = time()
    
        digraph = DiGraph()
        betweenness_centrality: dict = nx.betweenness_centrality(digraph)
        closeness_centrality: dict = nx.closeness_centrality(digraph)
        eigenvector_centrality: dict = nx.eigenvector_centrality(digraph)
        nodes = Node.objects.all()
        nodes_count = nodes.count()
    
        for inode, node in enumerate(nodes):
            sips = Vector.objects.filter(sip=node)
            dips = Vector.objects.filter(dip=node)
            node.outdegree = sips.count()
            node.indegree = dips.count()
            node.outgoing_weight = sips.aggregate(sum=Sum('drcpkts')).get('sum')
            node.incoming_weight = dips.aggregate(sum=Sum('srcpkts')).get('sum')
            node.betweenness_centrality = betweenness_centrality[str(node.ip)]
            node.closeness_centrality = closeness_centrality[str(node.ip)]
            node.eigenvector_centrality = eigenvector_centrality[str(node.ip)]
            node.save()
        
            if inode % 50 == 0:
                self.logger(f'{inode} processed from {nodes_count}')
    
        self.logger(f'Time left: {strftime("%H:%M:%S", gmtime(time() - start_time))}')