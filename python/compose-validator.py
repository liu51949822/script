#!/usr/bin/env python3
"""Docker Compose YAML Validator - 验证 docker compose 文件语法"""
import os, sys, yaml

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), 'docker')

def validate_file(path):
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
        svcs = data.get('services', {})
        nets = data.get('networks', {})
        return len(svcs), len(nets)
    except yaml.YAMLError as e:
        return f"YAML ERROR: {e}"
    except Exception as e:
        return f"ERROR: {e}"

def main():
    if not os.path.isdir(DOCKER_DIR):
        print(f"docker 目录不存在: {DOCKER_DIR}")
        sys.exit(1)
    
    print(f"{'服务':<30} {'服务数':<8} {'网络数':<8} {'状态'}")
    print('-' * 60)
    
    total, ok, fail = 0, 0, 0
    for name in sorted(os.listdir(DOCKER_DIR)):
        fpath = os.path.join(DOCKER_DIR, name, 'installcompose.file')
        if not os.path.isfile(fpath):
            continue
        total += 1
        result = validate_file(fpath)
        if isinstance(result, tuple):
            print(f"  {name:<28} {result[0]:<8} {result[1]:<8} ✅")
            ok += 1
        else:
            print(f"  {name:<28} {'-':<8} {'-':<8} ❌ {result}")
            fail += 1
    
    print('-' * 60)
    print(f"总计: {total}  有效: {ok}  失败: {fail}")

if __name__ == '__main__':
    main()
