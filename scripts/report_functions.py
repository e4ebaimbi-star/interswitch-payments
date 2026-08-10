
# ================================================
# report_functions.py
# Demonstrates functions by organising the report
# logic into named, reusable pieces.
# ================================================

# FUNCTION 1: Count entries by level
def count_log_levels(log_lines):
    """Count how many times each log level appears."""
    counts = {"SUCCESS": 0, "ERROR": 0, "WARNING": 0, "INFO": 0}
    for line in log_lines:
        if "[SUCCESS]" in line:
            counts["SUCCESS"] += 1
        elif "[ERROR]" in line:
            counts["ERROR"] += 1
        elif "[WARNING]" in line:
            counts["WARNING"] += 1
        elif "[INFO]" in line:
            counts["INFO"] += 1
    return counts

# FUNCTION 2: Collect failed directory names
def get_failed_dirs(log_lines):
    """Extract directory names from ERROR lines."""
    failed = []
    for line in log_lines:
        if "[ERROR]" in line and "Failed to back up:" in line:
            dir_name = line.split("Failed to back up:")[-1].strip()

            failed.append(dir_name)
    return failed

# FUNCTION 3: Determine health status
def get_health_status(error_count, warning_count):
    """Return GREEN, AMBER, or RED based on counts."""
    if error_count > 0:
        return "RED"
    elif warning_count > 0:
        return "AMBER"
    else:
        return "GREEN"

# FUNCTION 4: Print a formatted report section
def print_report_section(title, lines):
    """Print a titled section with a list of lines."""
    print(f"\n--- {title} ---")
    for line in lines:
        print(f" {line}")

# ================================================
# MAIN LOGIC: call the functions
# ================================================
log_lines = [
    "[2024-01-10 09:00:01] [SUCCESS] Backed up: src",
    "[2024-01-10 09:00:01] [SUCCESS] Backed up: docs",
    "[2024-01-10 09:00:02] [WARNING] Disk at 76%",
    "[2024-01-10 09:00:02] [ERROR] Failed to back up: logs",
    "[2024-01-10 09:00:03] [INFO] Backup complete",
]
# Call each function and store the results
counts = count_log_levels(log_lines)
failed = get_failed_dirs(log_lines)
status = get_health_status(counts["ERROR"], counts["WARNING"])
# Display the report
print("================================================")
print(f" Health Status: {status}")
print("================================================")
print_report_section("Counts", [
f"SUCCESS : {counts['SUCCESS']}",
f"WARNING : {counts['WARNING']}",
f"ERROR : {counts['ERROR']}",
])
if failed:
    print_report_section("Failed Directories", [f"- {d}" for d in failed])
else:
    print_report_section("Failed Directories", ["None"])
