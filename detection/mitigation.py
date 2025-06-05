import os
import logging
import time
from config import UNBLOCK_TIME, LOG_FILE
import subprocess

MALICIOUS_IP_FILE = "logs/malicious_ips.txt"

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

blocked_ips = {}

def block_ip(ip):
    """ Blocks an IP and schedules unblock """
    logging.warning(f"Blocking IP: {ip}")
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
    except Exception as e:
        logging.error(f"Failed to block IP {ip}: {e}")

def unblock_ips():
    """ Unblocks IPs after a cooldown period """
    current_time = time.time()
    for ip, block_time in list(blocked_ips.items()):
        if current_time - block_time > UNBLOCK_TIME:
            logging.warning(f"Unblocking IP: {ip}")
            os.system(f"sudo iptables -D INPUT -s {ip} -j DROP")
            del blocked_ips[ip]
