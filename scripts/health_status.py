
# ================================================
# health_status.py
# Determines the overall backup health status.
# GREEN = no errors and no warnings
# AMBER = warnings exist but no errors
# RED = one or more errors
# ================================================
# Backup counts (change these to test different statuses)
success_count = 3
error_count = 0
warning_count = 1
total_backups = 4
# Determine the health status
if error_count > 0:
	health_status = "RED"
	status_message =  "CRITICAL: One or more backups failed. Immediate action
required."
elif warning_count > 0:
	health_status = "AMBER"
	status_message = "WARNING: Backups completed but issues were detected.
Monitor closely."
else:
	health_status = "GREEN"
	status_message = "HEALTHY: All backups completed successfully. No issues
detected."
# Display the status
print("================================================")
print(f" Backup Health Status: {health_status}")
print("================================================")
print("")
print(f"Total attempted : {total_backups}")
print(f"Successful : {success_count}")
print(f"Warnings : {warning_count}")
print(f"Errors : {error_count}")

print("")
print(f"Status : {health_status}")
print(f"Message : {status_message}")
# Remind the team what action to take
print("")
print("--- Recommended Action ---")
if health_status == "RED":
	print("1. Check the log file immediately:
/tmp/interswitch_backups/backup.log")
	print("2. Identify which directories failed and why")
	print("3. Re-run the backup manually for failed directories")
	print("4. Notify the on-call engineer and the compliance team")
elif health_status == "AMBER":
	print("1. Review the warning entries in the log file")
	print("2. Check disk space on the backup server")
	print("3. Monitor tomorrow's backup closely")
else:
	print("No action required. All backups are healthy.")
