
# ================================================
# report_formatting.py
# Demonstrates f-strings for building report lines.
# ================================================
# Configuration values
company_name = "Interswitch"
report_date = "2024-01-10"
total_backups = 4
success_count = 3
error_count = 1
warning_count = 0
# Print a formatted report header
print("=" * 48) # prints 48 = signs
print(f" {company_name} Daily Backup Report")
print(f" Date: {report_date}")
print("=" * 48)
print("")
# Print formatted summary lines
print(f"Total backups attempted : {total_backups}")
print(f"Successful : {success_count}")
print(f"Errors : {error_count}")
print(f"Warnings : {warning_count}")
print("")
# Calculate and print the success rate
if total_backups > 0:
	success_rate = (success_count / total_backups) * 100
	print(f"Success rate : {success_rate:.1f}%")
else:
	print("Success rate : N/A (no backups attempted)")
# Demonstrate string operations on a sample log line
sample_line = " [2024-01-10 09:00:01] [SUCCESS] Backed up: src "
cleaned = sample_line.strip()
print("")
print("Sample log line (raw): ", repr(sample_line))
print("After .strip(): ", cleaned)
print("Contains SUCCESS? ", "SUCCESS" in cleaned)
print("Contains ERROR? ", "ERROR" in cleaned)
