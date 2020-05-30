from django.db import models


class Frame(models.Model):
    length = models.IntegerField(verbose_name='Length')
    destination = models.GenericIPAddressField(verbose_name='Destination')
    source = models.GenericIPAddressField(verbose_name='source')
    
    def __str__(self):
        return f'<Frame from {self.source} to {self.destination}, {self.length}>'
