import requests
from collections import defaultdict
import logging
import time
from scapy.all import IP, TCP, UDP, ICMP
from config import LOG_FILE, BASE_SYN_THRESHOLD, BASE_UDP_THRESHOLD, BASE_ICMP_THRESHOLD, ABUSEIPDB_API_KEY, ABUSEIPDB_CHECK_ENABLED

# Packet tracking
packet_counts = defaultdict(int)
last_reset_time = time.time()

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def check_ip_threat_intelligence(ip):
    """ Checks if an IP is reported as malicious using AbuseIPDB """
    if not ABUSEIPDB_CHECK_ENABLED:
        return False

    url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if data.get("data", {}).get("abuseConfidenceScore", 0) > 50:
            logging.warning(f"Threat Intelligence Alert: {ip} is flagged as malicious.")
            return True
    except Exception as e:
        logging.error(f"Error checking AbuseIPDB: {e}")
    
    return False

def update_thresholds():
    """ Adjust thresholds dynamically based on traffic """
    global BASE_SYN_THRESHOLD, BASE_UDP_THRESHOLD, BASE_ICMP_THRESHOLD
    BASE_SYN_THRESHOLD += 10  # Increase thresholds as traffic grows
    BASE_UDP_THRESHOLD += 20
    BASE_ICMP_THRESHOLD += 5

def detect_ddos(packet):
    """Detects DDoS attacks using adaptive thresholding"""
    global last_reset_time

    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    packet_counts[src_ip] += 1

    current_time = time.time()
    if current_time - last_reset_time > 60:  # Adjust every 60 seconds
        update_thresholds()
        last_reset_time = current_time

    if packet.haslayer(TCP) and packet[TCP].flags == 2:  # SYN Flood
        if packet_counts[src_ip] > BASE_SYN_THRESHOLD:
            logging.warning(f"SYN Flood detected from {src_ip}")
            return src_ip

    elif packet.haslayer(UDP):  # UDP Flood
        if packet_counts[src_ip] > BASE_UDP_THRESHOLD:
            logging.warning(f"UDP Flood detected from {src_ip}")
            return src_ip

    elif packet.haslayer(ICMP):  # ICMP Flood
        if packet_counts[src_ip] > BASE_ICMP_THRESHOLD:
            logging.warning(f"ICMP Flood detected from {src_ip}")
            return src_ip

    return None
