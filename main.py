from detection.packet_sniffer import capture_packets
from detection.detection_rules import detect_ddos
from detection.mitigation import block_ip, unblock_ips
import time
from scapy.all import IP

detected_ips = set()

def attack_handler(packet):
    """ Detects attacks and blocks IPs after checking Threat Intelligence """
    global detected_ips
    src_ip = packet[IP].src

    flagged_ip = detect_ddos(packet)
    if flagged_ip and flagged_ip not in detected_ips:
        block_ip(flagged_ip)
        detected_ips.add(flagged_ip)

# Continuous monitoring
while True:
    capture_packets(attack_handler)
    unblock_ips()
    time.sleep(30)
