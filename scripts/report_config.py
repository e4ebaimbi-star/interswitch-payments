
# ================================================
# report_config.py
# All configuration settings for the Interswitch
# daily backup report, stored as named variables.
# ================================================
# --- STRING variables ---
log_file_path = "/tmp/interswitch_backups/backup.log"
report_output_path = "/tmp/interswitch_backups/daily_report.txt"
company_name = "Interswitch"
report_title = "Daily Backup Health Report"
# --- INTEGER variables ---
total_backups = 0 # will be counted as we read the log
success_count = 3
error_count = 1
warning_count = 0
# --- BOOLEAN variables ---
report_ready = False # will be set to True when report is written
# --- FLOAT variable ---
success_rate = 0.0 # percentage of backups that succeeded
# Display the configuration
print("================================================")
print(" Report Configuration")
print("================================================")
print("")
print("Log file :", log_file_path)
print("Report output:", report_output_path)
print("Company :", company_name)

print("")
print("Starting counts:")
print(" Total :", total_backups)
print(" Success :", success_count)
print(" Errors :", error_count)
print(" Warnings :", warning_count)
print("")
print("Report ready :", report_ready)
