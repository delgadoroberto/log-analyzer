# 🔐 Log Analyzer

A lightweight Python-based log analysis tool designed to identify suspicious authentication activity from Linux SSH logs.

## Overview

This project parses authentication logs and identifies potentially malicious login attempts by analyzing failed password events and repeated source IP addresses.

It is intended as a simple cybersecurity practice project for learning Python, log parsing, and basic threat detection concepts commonly used in SOC and Blue Team environments.

## Features

- Detect failed login attempts
- Count authentication failures
- Identify repeated source IP addresses
- Highlight potential brute-force activity
- Generate a text-based security report
- Automatically create the reports directory if it does not exist

## Project Structure

```text
log-analyzer/
│
├── analyzer.py
├── sample_logs.txt
├── reports/
│   └── report.txt
└── README.md
```

## Sample Input

```text
Failed password for root from 192.168.1.10
Failed password for admin from 192.168.1.10
Accepted password for user from 192.168.1.15
Failed password for root from 10.0.0.5
Failed password for root from 192.168.1.10
Failed password for test from 10.0.0.5
```

## Usage

Clone the repository:

```bash
git clone https://github.com/delgadoroberto/log-analyzer.git
cd log-analyzer
```

Run the analyzer:

```bash
python3 analyzer.py
```

After execution, a report will be generated inside the `reports/` directory.

## Sample Output

```text
=== SECURITY LOG ANALYSIS ===

Failed login attempts: 5

Suspicious IPs:

192.168.1.10 -> 3 failed attempts
10.0.0.5 -> 2 failed attempts
```

## Security Concepts Covered

- Log analysis
- Authentication monitoring
- Brute-force attack detection
- IOC (Indicator of Compromise) identification
- Basic Blue Team workflows
- Python automation for cybersecurity

## Future Improvements

- JSON report export
- CSV report export
- Configurable detection thresholds
- Command-line arguments
- Support for real Linux `/var/log/auth.log` files
- GeoIP enrichment for source IP addresses

## Requirements

- Python 3.x

No external libraries are required.

## Author

**Roberto Delgado**

Senior Cybersecurity Consultant

Cybersecurity | Vulnerability Management | Cloud Security | DevSecOps | Security Engineering
