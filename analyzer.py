from collections import Counter
import re
import os

failed_attempts = 0
ips = []

os.makedirs("reports", exist_ok=True)

with open("sample_logs.txt", "r") as file:
    for line in file:

        if "Failed password" in line:
            failed_attempts += 1

            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

            if match:
                ips.append(match.group(1))

counter = Counter(ips)

report = []

report.append("=== SECURITY LOG ANALYSIS ===\n")
report.append(f"Failed login attempts: {failed_attempts}\n")
report.append("\nSuspicious IPs:\n")

for ip, count in counter.items():
    if count >= 2:
        report.append(f"{ip} -> {count} failed attempts\n")

with open("reports/report.txt", "w") as output:
    output.writelines(report)

print("Report generated successfully.")
