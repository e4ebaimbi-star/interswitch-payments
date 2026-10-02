# ================================================
# log_analyser.py
# Interswitch Daily Backup Log Analyser
# Author : Your Name
# Purpose : Reads the Interswitch backup log,
# counts entries by level, identifies
# failures, assigns a health status,
# and writes a formatted daily report.
# Usage : python3 scripts/log_analyser.py
# ================================================
import datetime

# ================================================
# CONFIGURATION
# ================================================
LOG_FILE = "interswitch_backups/backup.log"
REPORT_FILE = "interswitch_backups/daily_report.txt"
COMPANY = "Interswitch"
REPORT_DATE = datetime.date.today().strftime("%Y-%m-%d")
# ================================================
# FUNCTIONS


# ================================================
def read_log(log_path):
    """Read the log file and return all lines as a list."""
    try:
        with open(log_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"ERROR: Log file not found: {log_path}")
        return None
    except PermissionError:
        print(f"ERROR: Cannot read log file: {log_path}")
        return None
    except Exception as e:
        print(f"ERROR: Problem reading log: {e}")
        return None


def analyse_log(lines):
    """Count log levels and collect failed directory names."""
    counts = {"SUCCESS": 0, "ERROR": 0, "WARNING": 0, "INFO": 0}
    failed_dirs = []
    for line in lines:
        if "[SUCCESS]" in line:
            counts["SUCCESS"] += 1
        elif "[ERROR]" in line:
            counts["ERROR"] += 1
            if "Failed to back up:" in line:
                dir_name = line.split("Failed to back up:")[-1].strip()
                failed_dirs.append(dir_name)
        elif "[WARNING]" in line:
            counts["WARNING"] += 1
        elif "[INFO]" in line:
            counts["INFO"] += 1
    return counts, failed_dirs


def get_health_status(error_count, warning_count):
    """Return GREEN, AMBER, or RED based on error and warning counts."""
    if error_count > 0:
        return "RED", "CRITICAL: One or more backups failed."
    elif warning_count > 0:
        return "AMBER", "WARNING: Backups ran with warnings. Monitorclosely."
    else:
        return "GREEN", "HEALTHY: All backups completed successfully."


import os


def write_report(report_path, date, counts, failed_dirs, status, message, log_file):
    """Write the formatted daily report to a file."""
    lines = []
    lines.append("=" * 50)
    lines.append(f" {COMPANY} Daily Backup Health Report")
    lines.append(f" Date : {date}")
    lines.append(f" Status : {status}")
    lines.append("=" * 50)

    lines.append("")
    lines.append("--- Backup Summary ---")
    lines.append(f" Successful backups : {counts['SUCCESS']}")
    lines.append(f" Warnings : {counts['WARNING']}")
    lines.append(f" Errors : {counts['ERROR']}")
    lines.append("")
    lines.append("--- Health Assessment ---")
    lines.append(f" {message}")
    lines.append("")
    if failed_dirs:
        lines.append("--- Failed Directories ---")
        for d in failed_dirs:
            lines.append(f" - {d}")
        lines.append("")

    lines.append("--- Recommended Action ---")
    if status == "RED":
        lines.append(" 1. Check log file immediately: " + LOG_FILE)
        lines.append(" 2. Re-run failed backups manually")
        lines.append(" 3. Notify on-call engineer and compliance team")
    elif status == "AMBER":
        lines.append(" 1. Review warning entries in the log file")
        lines.append(" 2. Check disk space on backup server")
        lines.append(" 3. Monitor tomorrow's backup closely")
    else:
        lines.append(" No action required.")
        lines.append("")
        lines.append("=" * 50)
        lines.append(
            f" Report generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        lines.append("=" * 50)

    folder = os.path.dirname(report_path)
    os.makedirs(folder, exist_ok=True)
    try:
        abs_path = os.path.abspath(report_path)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"SUCCESS: Report written to {abs_path}")
        return True

    except Exception as e:
        print(f"ERROR: Could not write report: {e}")
        return False


# ================================================
# MAIN EXECUTION
# ================================================
print(f"Interswitch Log Analyser starting...")
print(f"Log file : {LOG_FILE}")
print(f"Report : {REPORT_FILE}")
print("")
# Step 1: Read the log file
lines = read_log(LOG_FILE)
if lines is None:
    print("Cannot continue without a log file. Exiting.")
    exit(1)
print(f"Read {len(lines)} lines from log file.")

# Step 2: Analyse the log
counts, failed_dirs = analyse_log(lines)
print(
    f"SUCCESS: {counts['SUCCESS']} | WARNING: {counts['WARNING']} |ERROR: {counts['ERROR']}"
)
# Step 3: Determine health status
status, message = get_health_status(counts["ERROR"], counts["WARNING"])
print(f"Health Status: {status}")
# Step 4: Write the report
success = write_report(
    REPORT_FILE, REPORT_DATE, counts, failed_dirs, status, message, LOG_FILE
)
if success:
    print(f"")
    print(f"Report written to: {REPORT_FILE}")
    print("Run 'cat " + REPORT_FILE + "' to view it.")
else:
    print("Report could not be written. Check permissions.")
    exit(1)
