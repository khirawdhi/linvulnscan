# LinVulnScan

A Python package to scan for Linux vulnerabilities and test privilege escalation vectors. It is based on the principles of LinPEAS but is customizable to your needs.

## Features

- Checks for Sudo misconfigurations
- Scans for SUID files
- Detects writable cron jobs and paths
- Creates a test user and tests escalation vectors
- Logs all actions to `vuln_scan_log.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/linvulnscan.git
    cd linvulnscan
    ```

2. Install the package:
    ```bash
    sudo pip install .
    ```

## Usage

Run the scanner:
```bash
sudo python3 -m linvulnscan
