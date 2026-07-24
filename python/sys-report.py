#!/usr/bin/env python3
"""
系统报告 - 生成详细的系统信息报告
生成日期: 2026-07-24
"""

import os
import sys
from pathlib import Path

import platform, os, json, subprocess, shutil
from datetime import datetime

def run_cmd(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=5)
        return r.stdout.strip()
    except: return "N/A"

def main():
    report = {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "cpu_count": os.cpu_count(),
        "python": platform.python_version(),
        "timestamp": datetime.now().isoformat(),
        "disk_usage": {},
    }
    if platform.system() == "Windows":
        report["windows_version"] = platform.version()
        for d in "CDEF":
            usage = shutil.disk_usage(f"{d}:\\") if os.path.exists(f"{d}:\\") else None
            if usage:
                report["disk_usage"][d] = {
                    "total_gb": round(usage.total / 1e9, 1),
                    "used_gb": round(usage.used / 1e9, 1),
                    "free_gb": round(usage.free / 1e9, 1),
                    "pct": round(usage.used / usage.total * 100, 1),
                }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
