# 🚨 DDoS Detection and Mitigation System

This project is a **real-time Distributed Denial of Service (DDoS) Detection and Mitigation System** built using Python (Scapy, Flask) and JavaScript (Chart.js) with dynamic thresholding, IP blocking, and a real-time monitoring dashboard.

---

## 📁 Project Structure

```text
ddos-detection/
│
├── detection/                 # Core detection & mitigation logic
│   ├── detection_rules.py     # DDoS detection logic with adaptive thresholding
│   ├── mitigation.py          # IP blocking/unblocking mechanisms
│   └── packet_sniffer.py      # Packet capture using Scapy
│
├── visualization/
│   └── visualize_logs.py      # Optional: Custom log visualizer (Not used in web dashboard)
│
├── logs/
│   └── ddos_logs.txt          # Logged attack events
│
├── web_dashboard/             # Flask-based real-time web dashboard
│   ├── static/
│   │   └── script.js          # Frontend JavaScript (Chart.js + auto-refresh)
│   ├── templates/
│   │   └── index.html         # HTML Dashboard page
│   └── app.py                 # Flask backend serving logs and data APIs
│
├── config.py                  # Configurations and adaptive thresholds
├── main.py                    # Main script to start detection loop
└── ddos-env/                  # Python virtual environment (recommended)

```

---

## 🚀 Features

- 🔍 **Real-Time DDoS Detection** using Scapy packet sniffing.
- 📊 **Adaptive Thresholds** that scale with network traffic volume.
- ⛔ **IP Blocking** with timed auto-unblock feature.
- 🌐 **Web Dashboard** for live monitoring of attack logs and frequency using Flask & Chart.js.
- 📁 **Log Management** to store and review suspicious activity.

---

## 🛠 Requirements

- Python 3.8+
- Install required libraries:

```bash
pip install scapy flask pandas

```bash
python -m venv ddos-env
source ddos-env/bin/activate  # On Windows: ddos-env\Scripts\activate

---

## ⚙️ How It Works

### 📡 Packet Sniffing
- Captures packets using `scapy.all.sniff()`.

### 🛡️ Detection
- Monitors **SYN**, **UDP**, and **ICMP** flood patterns.  
- Uses a **time-based adaptive threshold** that grows with traffic volume.

### 🚫 Mitigation
- Detected IPs are blocked.  
- After a cooldown (default **300 s**), IPs are automatically unblocked.

### 📝 Logging
- Attack events are stored in  
  `logs/ddos_logs.txt`.

### 📊 Visualization
- Dashboard refreshes every **5 seconds**, showing:  
  - 📊 **Attack frequency trends**  
  - 🧾 **Live log table**

---

## ▶️ Getting Started

### 1 . Start Detection Engine
```bash
python main.py
Starts packet sniffing, detection, and mitigation.

## 2. Launch Web Dashboard

```bash
cd web_dashboard
python app.py

Then open your browser at:  
📍 http://localhost:5000

## 📈 Web Dashboard Preview

- 📊 Bar Chart: real-time attack frequencies.
- 🧾 Log Table: timestamped attack events.
- Built with Chart.js (auto-refresh every 5 seconds).

---

## 📄 Key Files Explained

| File                    | Purpose                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------|
| `main.py`               | Launches detection loop; calls `capture_packets()` with `attack_handler()`.              |
| `detection_rules.py`    | Detects SYN, UDP, and ICMP floods; implements adaptive thresholding.                     |
| `mitigation.py`         | Handles IP blocking and automatic unblocking.                                            |
| `packet_sniffer.py`     | Lightweight wrapper around `scapy.sniff()`.                                              |
| `web_dashboard/app.py`  | Flask server providing APIs:  
  • `/api/logs` → logs JSON  
  • `/api/attack_data` → bar-chart data JSON                                              |

---

## 📌 Example Log Output

Location: `logs/ddos_logs.txt`
```bash
2025-06-05 15:23:01 - SYN Flood detected from 192.168.0.5
2025-06-05 15:24:05 - UDP Flood detected from 192.168.0.8


---

## 📊 Real-Time Monitoring (JS + Chart.js)

File: `static/script.js`

```js
setInterval(() => {
    fetchLogs();       // Update log table
    fetchAttackData(); // Update bar chart
}, 5000);              // Every 5 seconds


## 🧪 Test and Simulate

Simulate DDoS traffic only in a safe, isolated environment:

```bash
hping3 -S <target_ip> -p 80 --flood
⚠️ Use only on controlled networks or virtual labs.

---

## ✅ To Do / Future Enhancements

- Email alerts for critical attacks
- Better UI/UX styling
- Docker containerization
  - Authentication for dashboard access

---

## 🧠 Author & Contributions

**Sai Keerthan Reddy P**  
📧 saikeerthansk1@gmail.com  
🔗 [github.com/saikeerthan](https://github.com/saikeerthan)

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.  
Never deploy or test on public or production networks without proper authorization.
