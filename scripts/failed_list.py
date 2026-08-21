
# ================================================

# failed_list.py
# Demonstrates lists by collecting backup failures.
# ================================================
# Simulate backup results (we will read real log data in Section 10)
backup_results = [
	{"dir": "src", "status": "SUCCESS"},
	{"dir": "docs", "status": "SUCCESS"},
	{"dir": "logs", "status": "ERROR"},
	{"dir": "scripts", "status": "SUCCESS"},
	{"dir": "config", "status": "ERROR"},
]
# Start with empty lists
successful_dirs = []
failed_dirs = []
# Go through each result and sort into the right list
for result in backup_results:
	if result["status"] == "SUCCESS":
		successful_dirs.append(result["dir"])
	else:
		failed_dirs.append(result["dir"])
# Display the results
print("================================================")
print(" Backup Results Summary")
print("================================================")
print("")
print(f"Total processed: {len(backup_results)}")
print(f"Succeeded: {len(successful_dirs)}")
print(f"Failed: {len(failed_dirs)}")
print("")
if len(failed_dirs) > 0:
	print("Failed directories:")
	for d in failed_dirs:
		print(f" - {d}")
else:
	print("All directories backed up successfully.")
