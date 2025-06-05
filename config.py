import os

# Initial threshold values for adaptive thresholding
BASE_SYN_THRESHOLD = 100
BASE_UDP_THRESHOLD = 200
BASE_ICMP_THRESHOLD = 50

SYN_THRESHOLD = BASE_SYN_THRESHOLD
UDP_THRESHOLD = BASE_UDP_THRESHOLD
ICMP_THRESHOLD = BASE_ICMP_THRESHOLD

# Log file
LOG_FILE = "logs/ddos_logs.txt"

# Auto-unblock time (seconds)
UNBLOCK_TIME = 300  

# AbuseIPDB API Configuration
ABUSEIPDB_API_KEY = "your_abuseipdb_api_key_here"
ABUSEIPDB_CHECK_ENABLED = True  # Set to False to disable checking