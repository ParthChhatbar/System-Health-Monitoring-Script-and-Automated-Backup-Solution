#!/usr/bin/env python3

import psutil
import logging
from datetime import datetime

# -----------------------------
# Configuration / Thresholds
# -----------------------------
CPU_THRESHOLD = 80      # percent
MEMORY_THRESHOLD = 80   # percent
DISK_THRESHOLD = 90     # percent
LOG_FILE = "system_health.log"

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Functions
# -----------------------------
def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        alert = f"ALERT: CPU usage is high: {cpu_percent}%"
        print(alert)
        logging.warning(alert)

def check_memory():
    mem = psutil.virtual_memory()
    if mem.percent > MEMORY_THRESHOLD:
        alert = f"ALERT: Memory usage is high: {mem.percent}%"
        print(alert)
        logging.warning(alert)

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alert = f"ALERT: Disk usage is high: {disk.percent}%"
        print(alert)
        logging.warning(alert)

def check_processes():
    process_count = len(psutil.pids())
    # Optional: alert if too many processes (customize threshold)
    if process_count > 300:  # example threshold
        alert = f"ALERT: Too many processes running: {process_count}"
        print(alert)
        logging.warning(alert)

# -----------------------------
# Main Function
# -----------------------------
def main():
    print(f"Running system health check at {datetime.now()}")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    print("Check complete.\n")

if __name__ == "__main__":
    main()
