#Utility functions for command execution and logging.

import subprocess

def run_cmd(cmd, as_user=None):
    try:
        if as_user:
            cmd = f"sudo -u {as_user} {cmd}"
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode().strip()
    except subprocess.CalledProcessError:
        return ""

def log_output(title, content):
    with open("vuln_scan_log.txt", "a") as log:
        log.write(f"\n[+] {title}\n{content}\n")

