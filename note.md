1. install Django, pyshark and binary Tshark

* brew install wireshark [--with-qt] | Macos
* $PkgManager install wireshark | Linux


[Source CTU-Malware](https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-52/)

Packet example:
```yaml
Packet (Length: 60)
Layer ETH:
        Destination: 00:0b:46:42:f9:00
        Address: 00:0b:46:42:f9:00
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        Source: 00:1e:49:db:19:c1
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        Type: IPv4 (0x0800)
        Address: 00:1e:49:db:19:c1
Layer IP:
        0100 .... = Version: 4
        .... 0101 = Header Length: 20 bytes (5)
        Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
        Total Length: 40
        Identification: 0xacaa (44202)
        Flags: 0x4000, Don't fragment
        0... .... .... .... = Reserved bit: Not set
        .1.. .... .... .... = Don't fragment: Set
        ..0. .... .... .... = More fragments: Not set
        Fragment offset: 0
        Time to live: 127
        Protocol: TCP (6)
        Header checksum: 0xcc9a [validation disabled]
        Header checksum status: Unverified
        Source: 147.32.84.202
        Destination: 65.54.89.106
Layer TCP:
        Source Port: 1078
        Destination Port: 80
        Stream index: 0
        TCP Segment Len: 0
        Sequence number: 1    (relative sequence number)
        Sequence number (raw): 288186208
        Next sequence number: 1    (relative sequence number)
        Acknowledgment number: 1    (relative ack number)
        Acknowledgment number (raw): 1509449273
        0101 .... = Header Length: 20 bytes (5)
        Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        TCP Flags: \xc2\xb7\xc2\xb7\xc2\xb7\xc2\xb7\xc2\xb7\xc2\xb7\xc2\xb7A\xc2\xb7\xc2\xb7\xc2\xb7\xc2\xb7
        Window size value: 65535
        Calculated window size: 65535
        Window size scaling factor: -1 (unknown)
        Checksum: 0x0005 [unverified]
        Checksum Status: Unverified
        Urgent pointer: 0
        Timestamps
        Time since first frame in this TCP stream: 0.000000000 seconds
        Time since previous frame in this TCP stream: 0.000000000 seconds


```