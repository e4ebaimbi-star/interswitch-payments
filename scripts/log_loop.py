
# ================================================
# log_loop.py
# Loops through log lines, counts each level,
# and collects the names of failed directories.
# ================================================
# Simulated log lines
log_lines = [
    "[2024-01-10 09:00:00] [INFO] ===================================",
    "[2024-01-10 09:00:00] [INFO] Backup started - Run: 20240110_090000",
    "[2024-01-10 09:00:00] [INFO] Disk at 34% - healthy.",
    "[2024-01-10 09:00:01] [SUCCESS] Backed up: src",
    "[2024-01-10 09:00:01] [SUCCESS] Backed up: docs",
    "[2024-01-10 09:00:02] [WARNING] Disk at 76% - watch closely",
    "[2024-01-10 09:00:02] [ERROR] Failed to back up: logs",
    "[2024-01-10 09:00:03] [SUCCESS] Backed up: scripts",
    "[2024-01-10 09:00:03] [INFO] Done: 3 OK | 1 skipped | 1 failed",
    "[2024-01-10 09:00:03] [INFO] ===================================",
]
# Counters and collectors
counts = {"SUCCESS": 0, "ERROR": 0, "WARNING": 0, "INFO": 0}
failed_dirs = []
lines_processed = 0
# Process every line
for line in log_lines:
    line = line.strip() # remove leading/trailing whitespace
    lines_processed += 1
# Count the level
    if "[SUCCESS]" in line:
        counts["SUCCESS"] += 1
    elif "[ERROR]" in line:
        counts["ERROR"] += 1
# Extract the directory name from the error line
# Line format: [...] [ERROR] Failed to back up: dirname
if "Failed to back up:" in line:
    dir_name = line.split("Failed to back up:")[-1].strip()

    failed_dirs.append(dir_name)
elif "[WARNING]" in line:
    counts["WARNING"] += 1
elif "[INFO]" in line:
    counts["INFO"] += 1
# Display results
print("================================================")
print(" Log Analysis Results")
print("================================================")
print("")
print(f"Lines processed : {lines_processed}")
print(f"INFO : {counts['INFO']}")
print(f"SUCCESS : {counts['SUCCESS']}")
print(f"WARNING : {counts['WARNING']}")
print(f"ERROR : {counts['ERROR']}")
print("")
if failed_dirs:
    print(f"Failed directories ({len(failed_dirs)}):")
    for d in failed_dirs:
        print(f" - {d}")
else:
    print("No failed directories.")
