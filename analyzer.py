failed_attempts = 0

with open("sample_logs.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_attempts += 1

print(f"Failed login attempts: {failed_attempts}")
