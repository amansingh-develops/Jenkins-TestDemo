#!/usr/bin/env python3
"""
Pipeline Simulation Runner
Simulates the exact Jenkins Pipeline stages defined in the Jenkinsfile:
  1. Fetch / Verify Source Code from GitHub
  2. Workspace and Environment Inspection
  3. Automated Tests execution (test_form.py)
  4. Artifact Archival
  5. Post-Build status reporting
"""

import os
import subprocess
import sys
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_stage(num, total, name):
    print(f"\n{BOLD}{CYAN}[" + "=" * 50 + f"]{RESET}")
    print(f"{BOLD}{CYAN} Stage {num}/{total}: {name}{RESET}")
    print(f"{BOLD}{CYAN}[" + "=" * 50 + f"]{RESET}")


def run_stage(name, cmd):
    print(f"{YELLOW}> Executing: {cmd}{RESET}")
    start = time.time()
    res = subprocess.run(cmd, shell=True)
    duration = time.time() - start
    if res.returncode == 0:
        print(f"[PASS] Stage '{name}' completed successfully in {duration:.2f}s.")
        return True
    else:
        print(f"[FAIL] Stage '{name}' failed with exit code {res.returncode}.")
        return False


def main():
    print(f"\n{BOLD}Starting Jenkins Pipeline Simulation: [ amansingh-develops/Jenkins-TestDemo ]{RESET}")
    print("Pipeline definition: Jenkinsfile (Declarative Pipeline)")
    print(f"Agent: Local Agent (Windows/Any)\n")

    stages = [
        ("Checkout SCM / Git Verification", "git remote -v && git branch --show-current"),
        ("Environment & Runtime Verification", "python --version"),
        ("Automated Tests - Form Validation", "python test_form.py"),
        ("Archive Build Artifacts", "dir index.html style.css test_form.py Jenkinsfile"),
    ]

    for idx, (name, cmd) in enumerate(stages, 1):
        print_stage(idx, len(stages), name)
        success = run_stage(name, cmd)
        if not success:
            print(f"\n{RED}{BOLD}Pipeline execution FAILED at stage '{name}'{RESET}")
            sys.exit(1)

    print(f"\n{BOLD}{GREEN}============================================================{RESET}")
    print(f"{BOLD}{GREEN} PIPELINE RESULT: SUCCESS (All 4 stages passed!){RESET}")
    print(f"{BOLD}{GREEN} All required fields (Name, Email, Contact, Submit) verified.{RESET}")
    print(f"{BOLD}{GREEN}============================================================{RESET}\n")


if __name__ == '__main__':
    main()
