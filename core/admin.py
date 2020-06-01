from django.contrib import admin

from core.models import Frame, Node, Vector


class FrameAdmin(admin.ModelAdmin):
    list_display = ['length', 'destination', 'source']


# noinspection SpellCheckingInspection
class VectorAdmin(admin.ModelAdmin):
    list_display = ['sip', 'dip', 'srcpkts', 'drcpkts']


# noinspection SpellCheckingInspection
class NodeAdmin(admin.ModelAdmin):
    list_display = ['ip', 'outdegree', 'indegree', 'outgoing_weight', 'incoming_weight', 'betweenness_centrality',
                    'closeness_centrality', 'eigenvector_centrality', 'clustering_coefficient', 'alpha_centrality']


admin.site.register(Frame, FrameAdmin)
admin.site.register(Vector, VectorAdmin)
admin.site.register(Node, NodeAdmin)
