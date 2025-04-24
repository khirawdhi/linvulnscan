#Contains all the vulnerability scanning logic

import subprocess
import os
import shutil
from pathlib import Path
from .utils import run_cmd, log_output

USER_NAME = "vultestuser"
PASSWORD = "password"
LOG_FILE = "vuln_scan_log.txt"

def create_user():
    if shutil.which("useradd"):
        subprocess.run(f"useradd -m {USER_NAME}", shell=True)
        subprocess.run(f"echo '{USER_NAME}:{PASSWORD}' | chpasswd", shell=True)
        log_output("User Created", f"Created user {USER_NAME} with password '{PASSWORD}'")

def check_sudo_rights():
    output = run_cmd(f"sudo -l -U {USER_NAME}")
    log_output("Sudo Rights", output)
    if "NOPASSWD" in output:
        result = run_cmd("sudo /bin/bash -c 'whoami'", as_user=USER_NAME)
        log_output("Exploit: Sudo NOPASSWD", f"Result: {result}")

def check_suid_files():
    output = run_cmd("find / -perm -4000 -type f 2>/dev/null")
    log_output("SUID Binaries", output)

def check_cron_writable():
    output = run_cmd("find /etc/cron* -type f -writable 2>/dev/null")
    log_output("Writable Cron Jobs", output)

def check_path_hijack():
    output = run_cmd("echo $PATH | tr ':' '\\n'")
    writable_dirs = [line for line in output.splitlines() if os.access(line, os.W_OK)]
    hijack_log = "\n".join(writable_dirs)
    log_output("Writable PATH Dirs", hijack_log)
    if writable_dirs:
        test_path = Path(writable_dirs[0]) / "ls"
        with open(test_path, "w") as f:
            f.write("#!/bin/bash\necho 'Hacked by vultestuser'\n")
        os.chmod(test_path, 0o755)
        test_result = run_cmd("ls", as_user=USER_NAME)
        log_output("Exploit: PATH Hijack", test_result)
        os.remove(test_path)

def check_writable_dirs():
    output = run_cmd(f"sudo -u {USER_NAME} find / -writable -type d 2>/dev/null")
    log_output("Writable Directories as Normal User", output)

def clean_up():
    subprocess.run(f"userdel -r {USER_NAME}", shell=True)
    log_output("Cleanup", f"Removed user {USER_NAME}")

def run_scan():
    if os.geteuid() != 0:
        print("[!] This script must be run as root.")
        return

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    print("[*] Starting Vulnerability Scanner...\n")
    create_user()
    check_sudo_rights()
    check_suid_files()
    check_cron_writable()
    check_path_hijack()
    check_writable_dirs()
    clean_up()
    print(f"\n[+] Scan complete. Results saved in {LOG_FILE}")

