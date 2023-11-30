import psutil
import time

def get_network_connections():
    connections = psutil.net_connections(kind='inet')
    return connections

def display_network_activity():
    print("+++ Netzwerkaktivitäten +++")
    connections = get_network_connections()

    for conn in connections:
        print(f"Status: {conn.status}, Local Address: {conn.laddr}, Remote Address: {conn.raddr}")

def monitor_network_activity():
    while True:
        display_network_activity()
        time.sleep(10)  # Aktualisiere alle 10 Sekunden

if __name__ == "__main__":
    monitor_network_activity()
