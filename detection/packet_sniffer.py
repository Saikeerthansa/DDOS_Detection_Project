from scapy.all import sniff

def capture_packets(packet_handler, filter_rule="ip", duration=60):
    """ Captures packets and applies a detection function """
    print("[INFO] Monitoring network traffic...")
    sniff(filter=filter_rule, prn=packet_handler, store=0, timeout=duration)
