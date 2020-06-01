import logging

from django.core.management.base import BaseCommand

from core.utils.process import Preprocess

# Get an instance of a logger
logger = logging.getLogger('botnet')


class Command(BaseCommand):
    """ Upload pcap file"""
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--filename", action="store_true",
        )
    
    def handle(self, *args, **options):
        filename = options["filename"]
        if not filename:
            filename = "files/capture20110818-2.truncated.pcap"
        
        preprocess = Preprocess(logger=self.stdout.write)
        preprocess.frames_bulk_create(filename)
        preprocess.vectors_bulk_create()
        preprocess.upgrade_nodes()
        

        
        



