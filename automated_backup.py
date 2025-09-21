#!/usr/bin/env python3

import os
import shutil
import logging
from datetime import datetime
import paramiko  # for SSH/SCP backup
from scp import SCPClient

# -----------------------------
# Configuration
# -----------------------------
SOURCE_DIR = "/path/to/source_directory"      # Directory to backup
LOCAL_BACKUP_DIR = "/path/to/local_backup"    # Optional local backup folder
REMOTE_BACKUP = True                          # True to backup remotely
REMOTE_HOST = "remote.server.com"
REMOTE_USER = "username"
REMOTE_PASSWORD = "password"  # For simple password auth; SSH keys recommended
REMOTE_PATH = "/remote/backup/path"

LOG_FILE = "backup_report.log"

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Functions
# -----------------------------

def backup_local():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = os.path.join(LOCAL_BACKUP_DIR, f"backup_{timestamp}")
        shutil.copytree(SOURCE_DIR, dest)
        msg = f"Local backup successful: {dest}"
        print(msg)
        logging.info(msg)
    except Exception as e:
        msg = f"Local backup FAILED: {e}"
        print(msg)
        logging.error(msg)

def backup_remote():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        remote_dest = os.path.join(REMOTE_PATH, f"backup_{timestamp}")

        # Connect to remote server via SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST, username=REMOTE_USER, password=REMOTE_PASSWORD)

        # Use SCP to copy files
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(SOURCE_DIR, recursive=True, remote_path=remote_dest)

        msg = f"Remote backup successful: {REMOTE_HOST}:{remote_dest}"
        print(msg)
        logging.info(msg)

    except Exception as e:
        msg = f"Remote backup FAILED: {e}"
        print(msg)
        logging.error(msg)

# -----------------------------
# Main Function
# -----------------------------
def main():
    print(f"Starting backup at {datetime.now()}")

    # Backup locally
    backup_local()

    # Backup remotely if enabled
    if REMOTE_BACKUP:
        backup_remote()

    print("Backup operation completed.\n")

if __name__ == "__main__":
    main()
