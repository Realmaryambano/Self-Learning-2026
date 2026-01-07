# Program 6: Log Monitoring System
# Question: Monitor application logs and identify error frequency.

def count_errors(logs):
    return logs.count("ERROR")

def count_warnings(logs):
    return logs.count("WARNING")

def count_info(logs):
    return logs.count("INFO")

def system_health(errors):
    return "CRITICAL" if errors > 5 else "STABLE"

def log_analysis(logs):
    errors = count_errors(logs)
    warnings = count_warnings(logs)
    info = count_info(logs)
    return {
        "Errors": errors,
        "Warnings": warnings,
        "Info": info,
        "Health": system_health(errors)
    }

# Main Program
logs = ["INFO", "ERROR", "WARNING", "ERROR", "INFO", "ERROR"]
status = log_analysis(logs)
print(status)

# Output:
# {'Errors': 3, 'Warnings': 1, 'Info': 2, 'Health': 'STABLE'}
