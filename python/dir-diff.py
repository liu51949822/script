#!/usr/bin/env python3
"""
目录对比 - 递归对比两个目录差异
生成日期: 2026-07-24
"""

import os
import sys
from pathlib import Path

import os, hashlib, sys

def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_dir(root):
    result = {}
    for dirpath, _, files in os.walk(root):
        for f in files:
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, root)
            result[rel] = file_hash(full)
    return result

def main():
    if len(sys.argv) < 3:
        print("用法: python dir-diff.py <目录A> <目录B>")
        return
    a, b = sys.argv[1], sys.argv[2]
    fa, fb = scan_dir(a), scan_dir(b)
    only_a = set(fa) - set(fb)
    only_b = set(fb) - set(fa)
    diff = {k for k in fa if k in fb and fa[k] != fb[k]}
    print(f"仅在 {a}: {len(only_a)} 文件")
    for f in sorted(only_a)[:10]: print(f"  - {f}")
    print(f"仅在 {b}: {len(only_b)} 文件")
    for f in sorted(only_b)[:10]: print(f"  - {f}")
    print(f"内容不同: {len(diff)} 文件")
    for f in sorted(diff)[:10]: print(f"  ~ {f}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
