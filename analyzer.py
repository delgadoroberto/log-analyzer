from collections import Counter
import re

failed_attempts = 0
ips = []

with open("sample_logs.txt", "r") as file:
    for line in file:

        if "Failed password" in line:
            failed_attempts += 1

            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

            if match:
                ips.append(match.group(1))

print(f"\nFailed login attempts: {failed_attempts}")

counter = Counter(ips)

print("\nSuspicious IPs:")

for ip, count in counter.items():
    if count >= 2:
        print(f"{ip} -> {count} failed attempts")
