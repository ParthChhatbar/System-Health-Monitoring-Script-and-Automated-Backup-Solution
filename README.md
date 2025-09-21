# System-Health-Monitoring-Script-and-Automated-Backup-Solution

This repository contains **two Linux automation scripts** implemented in Python:  

1. **System Health Monitoring Script** – monitors CPU, memory, disk, and running processes.  
2. **Automated Backup Solution** – backs up a specified directory to a local or remote location and generates a report.  

Both scripts are configurable, log their actions, and can be scheduled via cron or other schedulers.

---

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Prerequisites](#1-prerequisites)
  - [2. System Health Monitoring Script](#2-system-health-monitoring-script)
  - [3. Automated Backup Script](#3-automated-backup-script)
- [Logging](#logging)
- [Optional Enhancements](#optional-enhancements)
- [License](#license)

---

## Project Overview
These scripts automate common Linux administrative tasks:

### 1. System Health Monitoring
- Monitors:
  - CPU usage
  - Memory usage
  - Disk usage
  - Running processes
- Alerts when thresholds are exceeded.
- Logs alerts to a file and prints them to the console.

### 2. Automated Backup Solution
- Backs up a source directory to:
  - Local backup folder  
  - Remote server via SSH/SCP
- Creates **timestamped backups**.
- Logs success or failure for each operation.

---

## Repository Structure
```
.
├─ system_health_monitor.py       # Objective 1: System health monitoring script
├─ automated_backup.py            # Objective 2: Automated backup script
├─ README.md                      # Project documentation
└─ logs/
   ├─ system_health.log           # System health alerts log
   └─ backup_report.log           # Backup success/failure log
```

---

## Setup Instructions

### 1. Prerequisites
- Python 3.x installed
- Linux environment (Ubuntu/CentOS/etc.)
- Optional for backup script: `paramiko` and `scp` Python packages

Install required Python packages:
```bash
pip install psutil paramiko scp
```

---

### 2. System Health Monitoring Script

**File:** `system_health_monitor.py`

**Features:**
- Monitors CPU, memory, disk usage, and running processes.
- Alerts when thresholds are exceeded.
- Logs alerts to `logs/system_health.log`.

**Run the script:**
```bash
python3 system_health_monitor.py
```

**Optional: Schedule via cron (every 5 minutes):**
```bash
*/5 * * * * /usr/bin/python3 /path/to/system_health_monitor.py
```

---

### 3. Automated Backup Script

**File:** `automated_backup.py`

**Features:**
- Backs up a source directory to local and/or remote destination.
- Creates timestamped backup directories.
- Logs success/failure to `logs/backup_report.log`.

**Configure the script:**
- Update `SOURCE_DIR` with the folder you want to backup.
- Set `LOCAL_BACKUP_DIR` for local backup.
- For remote backup, set `REMOTE_BACKUP=True` and configure:
  - `REMOTE_HOST`
  - `REMOTE_USER`
  - `REMOTE_PASSWORD` (or use SSH keys)
  - `REMOTE_PATH`

**Run the script:**
```bash
python3 automated_backup.py
```

**Optional: Schedule via cron (daily at 2 AM):**
```bash
0 2 * * * /usr/bin/python3 /path/to/automated_backup.py
```

---

## Logging
Both scripts log their actions in the `logs/` folder:
- `logs/system_health.log` – records alerts from system health checks.
- `logs/backup_report.log` – records success or failure of backup operations.

Logs include **timestamps**, **alert messages**, and **error information** if any operation fails.

---

## Optional Enhancements
- **System Health Script:**
  - Send email or SMS alerts when thresholds are exceeded.
  - Run continuously in the background with configurable intervals.
- **Backup Script:**
  - Compress backup folders to `.tar.gz` before transfer.
  - Use SSH keys for secure remote authentication.
  - Integrate with cloud storage (AWS S3, Google Drive, etc.)

---

## License
This project is licensed under the [MIT License](LICENSE).
