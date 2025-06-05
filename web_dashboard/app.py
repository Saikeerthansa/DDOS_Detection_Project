from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

LOG_FILE = "../logs/ddos_logs.txt"
MALICIOUS_IP_FILE = "logs/malicious_ips.txt"

def get_logs():
    """Fetches log data for dashboard"""
    try:
        df = pd.read_csv(LOG_FILE, sep=" - ", engine="python", names=["timestamp", "event"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df.to_dict(orient="records")
    except:
        return []
        
def get_malicious_ips():
    try:
        with open(MALICIOUS_IP_FILE, "r") as f:
            return [ip.strip() for ip in f.readlines()]
    except:
        return []

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/logs")
def logs_api():
    """API endpoint for logs"""
    logs = get_logs()
    return jsonify(logs)
    
@app.route("/api/malicious_ips")
def malicious_ips_api():
    return jsonify(get_malicious_ips())

@app.route("/api/attack_data")
def attack_data():
    """Returns attack count data"""
    try:
        df = pd.read_csv(LOG_FILE, sep=" - ", engine="python", names=["timestamp", "event"])
        attack_counts = df["event"].value_counts().to_dict()
        return jsonify(attack_counts)
    except:
        return jsonify({})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

