import dataclasses
import time
from typing import Optional, Generator, Any

import pyshark


@dataclasses.dataclass
class Frame:
    length: str
    destination: str
    source: str
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)


class PcapFileCapture:
    def __init__(self, filename: str = None, limit: Optional[int] = None):
        assert filename is not None
        self.limit = limit
        self.start_time = time.time()
        self.cap_file = pyshark.FileCapture(filename, keep_packets=True, use_json=True)
        
    def read(self) -> Generator[Frame, Any, None]:
        for ic, pkt in enumerate(self.cap_file):
            
            if self.limit and ic > self.limit-1:
                break
                
            for layer in pkt.layers:
                if layer._layer_name == 'ip':
                    yield Frame(length=pkt.length, destination=layer.dst, source=layer.src)
