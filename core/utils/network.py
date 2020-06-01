
import networkx as nx
import pylab as plt
from core.models import Vector


class DiGraph:
    def __init__(self):
        self.digraph = nx.DiGraph(self._get_edges())
    
    @staticmethod
    def _get_edges():
        # noinspection PyShadowingNames
        edges = []
        for vector in Vector.objects.all():
            edges.append((str(vector.sip.ip), str(vector.dip.ip), {'weight': vector.srcpkts}))
            if vector.drcpkts != 0:
                edges.append((str(vector.dip.ip), str(vector.sip.ip), {'weight': vector.drcpkts}))
        return edges
    
    def get_info_graph(self):
        return self.digraph.number_of_nodes(), self.digraph.number_of_edges()
    
    def get_graph(self):
        return self.digraph
    
    def get_graph_edges(self):
        return self.digraph.edges(data=True)
