from collections import Counter
import os
import re


def analyze_logs(logfile):
    failed_attempts = 0
    successful_logins = 0
    sudo_executions = 0

    failed_ips = []
    all_ips = []

    with open(logfile, "r") as file:
        for line in file:

            # Failed SSH logins
            if "Failed password" in line:
                failed_attempts += 1

                match = re.search(
                    r'from (\d+\.\d+\.\d+\.\d+)',
                    line
                )

                if match:
                    ip = match.group(1)
                    failed_ips.append(ip)
                    all_ips.append(ip)

            # Successful SSH logins
            elif "Accepted password" in line or "Accepted publickey" in line:
                successful_logins += 1

                match = re.search(
                    r'from (\d+\.\d+\.\d+\.\d+)',
                    line
                )

                if match:
                    all_ips.append(match.group(1))

            # Sudo activity
            elif "sudo:" in line and "COMMAND=" in line:
                sudo_executions += 1

    return (
        failed_attempts,
        successful_logins,
        sudo_executions,
        Counter(failed_ips),
        Counter(all_ips)
    )


def get_severity(count):
    if count >= 10:
        return "HIGH"
    elif count >= 5:
        return "MEDIUM"
    elif count >= 2:
        return "LOW"
    else:
        return None


def generate_report(
    failed_attempts,
    successful_logins,
    sudo_executions,
    failed_ip_counter,
    all_ip_counter
):
    report = []

    report.append("========================================\n")
    report.append("      SECURITY LOG ANALYSIS REPORT\n")
    report.append("========================================\n\n")

    report.append(
        f"Successful SSH logins : {successful_logins}\n"
    )
    report.append(
        f"Failed SSH logins     : {failed_attempts}\n"
    )
    report.append(
        f"Sudo executions       : {sudo_executions}\n\n"
    )

    report.append("Top source IPs\n\n")

    if all_ip_counter:
        for ip, count in all_ip_counter.most_common(5):
            report.append(f"{ip:<15} : {count} events\n")
    else:
        report.append("No IP activity detected.\n")

    report.append("\n")
    report.append("Potential brute-force sources\n\n")

    suspicious_found = False

    for ip, count in failed_ip_counter.items():
        severity = get_severity(count)

        if severity:
            suspicious_found = True
            report.append(
                f"[{severity}] {ip:<15} : {count} failed attempts\n"
            )

    if not suspicious_found:
        report.append("No suspicious activity detected.\n")

    report.append("\n")
    report.append("Analysis completed successfully.\n")

    return report


def main():

    os.makedirs("reports", exist_ok=True)

    logfile = "sample_logs.txt"

    (
        failed_attempts,
        successful_logins,
        sudo_executions,
        failed_ip_counter,
        all_ip_counter
    ) = analyze_logs(logfile)

    report = generate_report(
        failed_attempts,
        successful_logins,
        sudo_executions,
        failed_ip_counter,
        all_ip_counter
    )

    with open("reports/report.txt", "w") as output:
        output.writelines(report)

    print("[+] Security analysis completed.")
    print("[+] Report saved to reports/report.txt")


if __name__ == "__main__":
    main()
