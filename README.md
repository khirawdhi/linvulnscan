# LinVulnScan

A lightweight Python tool for identifying and validating common Linux privilege escalation misconfigurations during authorized security assessments.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Features

* Detects common privilege escalation risks:

  * SUID/SGID binaries
  * `sudo` misconfigurations
  * World-writable files and directories
  * Cron jobs
  * Basic kernel version checks
* Validates potential privilege escalation paths using a temporary non-root user
* Generates a scan report

---

## Installation

```bash
pip install git+https://github.com/khirawdhi/linvulnscan.git
```

Or install locally:

```bash
git clone https://github.com/khirawdhi/linvulnscan.git
cd linvulnscan
sudo pip install .
```

---

## Usage

```bash
sudo run_scan
```

or

```bash
sudo python3 -m linvulnscan
```

> Root privileges are required for system inspection and validation.

---

## Example Output

```text
[+] SUID Binary Found: /usr/bin/sudo
[+] Potential privilege escalation path detected
[+] Validation completed successfully
```

---

## Disclaimer

LinVulnScan is intended for **authorized security assessments, security research, CTFs, and lab environments only**. Use only on systems you own or have explicit permission to test.

---

## License

MIT
