import matplotlib.pyplot as plt
import pandas as pd

def visualize_attacks(log_file):
    """ Visualizes attack trends in real-time """
    df = pd.read_csv(log_file, sep=" - ", engine="python", names=["timestamp", "event"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["event"].value_counts().plot(kind="bar", color="red")

    plt.title("DDoS Attack Trends")
    plt.xlabel("Attack Type")
    plt.ylabel("Frequency")
    plt.show()

# Example: visualize_attacks("logs/ddos_logs.txt")
