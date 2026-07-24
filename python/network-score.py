#!/usr/bin/env python3
"""
网络评分 - 测试网络质量并评分
生成日期: 2026-07-24
"""

import os
import sys
from pathlib import Path

import subprocess, json, time

def ping_test(host="8.8.8.8", count=4):
    cmd = ["ping", "-n", str(count), host]
    r = subprocess.run(cmd, capture_output=True, text=True)
    times = []
    for line in r.stdout.split("\n"):
        if "time=" in line.lower() or "ms" in line.lower():
            parts = line.split()
            for p in parts:
                if "ms" in p:
                    try:
                        t = p.replace("ms", "").replace("time=", "")
                        times.append(float(t))
                    except: pass
    return {"avg": sum(times)/len(times) if times else 0, "packet_loss": 100 - len(times)*25}

def main():
    result = ping_test()
    score = 100
    if result["avg"] > 200: score -= 30
    elif result["avg"] > 100: score -= 15
    elif result["avg"] > 50: score -= 5
    if result["packet_loss"] > 0: score -= result["packet_loss"]
    print(json.dumps({"score": max(0, score), "avg_ms": result["avg"], "loss_pct": result["packet_loss"]}, indent=2))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
