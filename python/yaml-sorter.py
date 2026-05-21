#!/usr/bin/env python3
"""YAML Sorter - 对 Docker Compose 文件中的 services 按字母排序"""
import os, sys, yaml

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), 'docker')

def sort_compose_file(fpath):
    with open(fpath) as f:
        data = yaml.safe_load(f)
    
    if 'services' in data and isinstance(data['services'], dict):
        data['services'] = dict(sorted(data['services'].items()))
    if 'networks' in data and isinstance(data['networks'], dict):
        data['networks'] = dict(sorted(data['networks'].items()))
    
    with open(fpath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def main():
    if not os.path.isdir(DOCKER_DIR):
        print(f"docker 目录不存在: {DOCKER_DIR}")
        sys.exit(1)
    
    count = 0
    for name in sorted(os.listdir(DOCKER_DIR)):
        fpath = os.path.join(DOCKER_DIR, name, 'installcompose.file')
        if not os.path.isfile(fpath):
            continue
        try:
            sort_compose_file(fpath)
            print(f"  ✅ {name}")
            count += 1
        except Exception as e:
            print(f"  ❌ {name}: {e}")
    
    print(f"已排序 {count} 个文件")

if __name__ == '__main__':
    main()
