import logging
from time import gmtime, strftime, time

from django.core.management.base import BaseCommand

from django.db.models import Q

from core.models import Frame, Vector, Node
from core.network_utils.pcap_read import PcapFileCapture

# Get an instance of a logger
logger = logging.getLogger('botnet')


class Command(BaseCommand):
    """ Upload pcap file"""
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--filename", action="store_true",
        )
    
    def frames_bulk_create(self, filename):
        if Frame.objects.exists():
            self.stdout.write(f'{Frame.objects.count()} frames has been deleted')
            Frame.objects.all().delete()
    
        pcap_file = PcapFileCapture(filename=filename, limit=100000)
        frames: list = []
        for ic, frame in enumerate(pcap_file.read()):
            # pass
            self.stdout.write(f'Frame {ic} -> {frame.as_dict()}')
            frames.append(Frame(**frame.as_dict()))

        Frame.objects.bulk_create(frames)

        self.stdout.write(f'Time left: {strftime("%H:%M:%S", gmtime(time() - pcap_file.start_time))}')
    
    def vectors_bulk_create(self):
        start_time = time()
        if Vector.objects.exists():
            self.stdout.write(f'{Vector.objects.count()} vectors has been deleted')
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
                self.stdout.write(f'{ic} processed from {frames_count}')
        
        self.stdout.write(f'Time left: {strftime("%H:%M:%S", gmtime(time() - start_time))}')
    
    def handle(self, *args, **options):
        filename = options["filename"]
        if not filename:
            filename = "files/capture20110818-2.truncated.pcap"
        
        self.frames_bulk_create(filename)
        self.vectors_bulk_create()
        

        
        



