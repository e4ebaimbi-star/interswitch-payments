
# ================================================
# log_counter.py
# Uses a dictionary to count log entry levels.
# ================================================
# Start with all counts at zero
counts = {
	"SUCCESS": 0,
	"ERROR": 0,
	"WARNING": 0,
	"INFO": 0
}
# Simulated log lines (we will read real ones from file in Section 10)
log_lines = [
	"[2024-01-10 09:00:00] [INFO] Backup started",
	"[2024-01-10 09:00:01] [SUCCESS] Backed up: src",
	"[2024-01-10 09:00:01] [SUCCESS] Backed up: docs",
	"[2024-01-10 09:00:02] [WARNING] Disk at 76% - monitor closely",
	"[2024-01-10 09:00:02] [SUCCESS] Backed up: scripts",
	"[2024-01-10 09:00:03] [ERROR] Failed to back up: logs",
	"[2024-01-10 09:00:03] [INFO] Backup complete",
]
# Loop through each line and count by level
for line in log_lines:
	if "[SUCCESS]" in line:
		counts["SUCCESS"] += 1
	elif "[ERROR]" in line:
		counts["ERROR"] += 1
	elif "[WARNING]" in line:
		counts["WARNING"] += 1
	elif "[INFO]" in line:
		counts["INFO"] += 1
# Display the counts
print("================================================")
print(" Log Entry Count")
print("================================================")
print("")
print(f"INFO entries : {counts['INFO']}")
print(f"SUCCESS entries : {counts['SUCCESS']}")
print(f"WARNING entries : {counts['WARNING']}")
print(f"ERROR entries : {counts['ERROR']}")
print("")
print(f"Total lines processed: {len(log_lines)}")
