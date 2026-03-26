LinVulnScan — Linux Privilege Escalation Scanner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/khirawdhi/linvulnscan)](https://github.com/khirawdhi/linvulnscan/issues)

`LinVulnScan` is a Python-based lightweight Linux privilege escalation discovery tool inspired by [linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS).  
It identifies common misconfigurations, insecure binaries, SUID issues, and then **automatically tests** privilege escalation vectors using a **non-root user** created during runtime.

---

## Features

- Checks for:
  - SUID/SGID binaries
  - World-writable files and paths
  - sudo misconfigurations
  - Cron jobs and scripts
  - Kernel exploits (basic check)
- Automatically creates a temp user to **test vulnerabilities**
- Attempts to exploit verified escalation vectors (ethically)
- Generates a scan report

---

## Installation

Install directly from GitHub:

pip install git+https://github.com/khirawdhi/linvulnscan.git
```

Or clone the repository manually and install locally:

git clone https://github.com/khirawdhi/linvulnscan.git
cd linvulnscan
sudo pip install .
```

---

## Usage

Once installed, run the scanner using the following commands:

```bash
sudo run_scan
```

or

```bash
sudo python3 -m linvulnscan
```

> **Note:** Root access is required to run escalation checks.

---

## Sample Output

Here is a sample of what the output will look like when the scanner runs:

```bash
[+] SUID Binary Found: /usr/bin/sudo
[+] Exploitable with sudo misconfig
[+] Attempting privilege escalation as user: tempuser
[+] Escalation successful. User tempuser gained root access.
```

---

## Ethical Use

`LinVulnScan` is intended for **authorized security assessments**, **Capture the Flag (CTF) competitions**, and **lab testing** only.  
**Please do not use this tool on systems you do not own or have explicit permission to test.** Unauthorized use is illegal and unethical.

---

## Author

**Khirawdhi Ray**  
Website: [raykhira.com](https://raykhira.com/)  
GitHub: [@khirawdhi](https://github.com/khirawdhi)  
LinkedIn: [linkedin.com/in/khirawdhi](https://www.linkedin.com/in/khirawdhi/)

---


