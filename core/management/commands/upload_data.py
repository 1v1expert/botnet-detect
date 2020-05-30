import logging
from time import gmtime, strftime, time

from django.core.management.base import BaseCommand

from core.models import Frame
from core.network_utils.pcap_read import PcapFileCapture

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
            
        if Frame.objects.exists:
            self.stdout.write(f'{Frame.objects.count()} has been deleted')
            Frame.objects.all().delete()
            
        pcap_file = PcapFileCapture(filename=filename)
        frames: list = []
        for ic, frame in enumerate(pcap_file.read()):
            # pass
            self.stdout.write(f'Frame {ic} -> {frame.as_dict()}')
            frames.append(Frame(**frame.as_dict()))
        
        Frame.objects.bulk_create(frames)

        self.stdout.write(f'Time left: {strftime("%H:%M:%S", gmtime(time() - pcap_file.start_time))}')
        



