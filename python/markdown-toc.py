#!/usr/bin/env python3
import sys, re, os

def generate_toc(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    
    toc = []
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.+)', line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        anchor = title.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        toc.append((level, title, anchor))
    
    if not toc:
        print("未找到标题 (## Title)")
        return
    
    print(f"<!-- TOC 生成自 {os.path.basename(filepath)} -->\n")
    for level, title, anchor in toc:
        indent = "  " * (level - 2) if level >= 2 else ""
        print(f"{indent}- [{title}](#{anchor})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python markdown-toc.py README.md")
        sys.exit(1)
    generate_toc(sys.argv[1])
