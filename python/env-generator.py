#!/usr/bin/env python3
"""Environment Variable Generator - 从 docker compose 文件提取并生成 .env 示例"""
import os, sys, re

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), 'docker')
OUTPUT = os.path.join(DOCKER_DIR, '.env.example')

VAR_PATTERN = re.compile(r'\$\{(\w+)(?::[^}]*)?\}')

def extract_vars(content):
    return set(VAR_PATTERN.findall(content))

def main():
    all_vars = set()
    count = 0
    for name in sorted(os.listdir(DOCKER_DIR)):
        fpath = os.path.join(DOCKER_DIR, name, 'installcompose.file')
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            vars_found = extract_vars(f.read())
        if vars_found:
            all_vars.update(vars_found)
            count += 1
    
    lines = ['# Docker Compose 环境变量示例', f'# 生成自 {count} 个服务', '']
    for var in sorted(all_vars):
        lines.append(f'{var}=change_me')
    
    with open(OUTPUT, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    
    print(f"已生成 {OUTPUT} ({len(all_vars)} 个变量)")

if __name__ == '__main__':
    main()
