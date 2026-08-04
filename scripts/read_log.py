
# ================================================
# read_log.py
# Reads the real Interswitch backup log file
# and displays every line with its number.

# ================================================
log_file = "/tmp/interswitch_backups/backup.log"
print(f"Reading log file: {log_file}")
print("================================================")
print("")
try:
    with open(log_file, "r") as f:
        line_number = 0
        for line in f:
            line_number += 1
            clean_line = line.strip()
            print(f"{line_number:3} {clean_line}")
    print("")
    print(f"Total lines in log: {line_number}")
except FileNotFoundError:
    print(f"ERROR: Log file not found: {log_file}")
    print("Make sure the backup script has run at least once.")
except PermissionError:
    print(f"ERROR: Cannot read log file. Check permissions: {log_file}")
except Exception as e:
    print(f"ERROR: Unexpected problem reading log: {e}")
