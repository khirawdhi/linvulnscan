# 🔍 LinVulnScan — Linux Privilege Escalation Scanner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/khirawdhi/linvulnscan)](https://github.com/khirawdhi/linvulnscan/issues)

`LinVulnScan` is a Python-based lightweight Linux privilege escalation discovery tool inspired by [linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS).  
It identifies common misconfigurations, insecure binaries, SUID issues, and then **automatically tests** privilege escalation vectors using a **non-root user** created during runtime.

---

## 🚀 Features

- 🔐 Checks for:
  - SUID/SGID binaries
  - World-writable files and paths
  - sudo misconfigurations
  - Cron jobs and scripts
  - Kernel exploits (basic check)
- 🧪 Automatically creates a temp user to **test vulnerabilities**
- 🔁 Attempts to exploit verified escalation vectors (ethically)
- 📝 Generates a scan report

---

## ⚙️ Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/khirawdhi/linvulnscan.git
