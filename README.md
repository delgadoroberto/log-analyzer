# 🔐 Log Analyzer

A lightweight Python-based log analysis tool designed to identify suspicious authentication activity from Linux SSH logs.

## Overview

Log Analyzer parses Linux authentication logs and identifies potentially malicious login attempts by analyzing failed password events and repeated source IP addresses.

This project was created as a cybersecurity practice tool to demonstrate basic log parsing, threat detection, and security automation concepts commonly used in SOC and Blue Team environments.

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
├── examples/
│   └── auth.log
├── reports/
│   └── report.txt
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

## Included Datasets

### sample_logs.txt

A small synthetic dataset intended for quick testing and development.

Example:

```text
Failed password for root from 192.168.1.10
Failed password for admin from 192.168.1.10
Accepted password for user from 192.168.1.15
Failed password for root from 10.0.0.5
Failed password for root from 192.168.1.10
Failed password for test from 10.0.0.5
```

### examples/auth.log

A larger and more realistic Linux authentication log used for parser validation and analysis practice.

The dataset contains typical authentication events such as:

- SSH daemon startup
- Successful SSH logins
- Failed SSH login attempts
- PAM session events
- sudo command executions
- User session creation and termination

Example:

```text
Mar 27 13:08:09 ip-10-77-20-248 sshd[1361]: Accepted publickey for ubuntu from 85.245.107.41 port 54259 ssh2
Mar 27 13:09:37 ip-10-77-20-248 sudo: ubuntu : TTY=pts/0 ; USER=root ; COMMAND=/usr/bin/curl
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

- Linux authentication logs
- Log analysis
- SSH monitoring
- Authentication monitoring
- Brute-force attack detection
- IOC (Indicator of Compromise) identification
- Basic Blue Team workflows
- Python automation for cybersecurity

## Future Improvements

- Successful login tracking
- SSH session statistics
- sudo activity analysis
- Top targeted usernames
- JSON report export
- CSV report export
- Configurable detection thresholds
- Command-line arguments
- Native support for `/var/log/auth.log`
- GeoIP enrichment for source IP addresses

### Example of a future report

```text
========================================
      SECURITY LOG ANALYSIS REPORT
========================================

Successful SSH logins : 15
Failed SSH logins     : 42

Top source IPs

85.245.107.41 : 12 events
192.168.1.10  : 8 events

Sudo executions : 31

Potential brute-force sources

203.0.113.25 : 18 failed attempts
```

## Requirements

- Python 3.x

No external libraries are required.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Roberto Delgado**

Senior Cybersecurity Consultant

Cybersecurity | Vulnerability Management | Cloud Security | DevSecOps | Security Engineering
