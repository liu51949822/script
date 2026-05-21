#!/usr/bin/env python3
"""Config Backup Script - 备份所有 docker compose 配置文件"""
import os, sys, tarfile, datetime

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
BACKUP_DIR = os.path.join(ROOT_DIR, 'backups')

def create_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"docker_compose_backup_{timestamp}.tar.gz"
    filepath = os.path.join(BACKUP_DIR, filename)
    
    with tarfile.open(filepath, 'w:gz') as tar:
        docker_dir = os.path.join(ROOT_DIR, 'docker')
        for item in os.listdir(docker_dir):
            fpath = os.path.join(docker_dir, item, 'installcompose.file')
            if os.path.isfile(fpath):
                tar.add(fpath, arcname=f"docker/{item}/installcompose.file")
    
    size = os.path.getsize(filepath)
    return filepath, size

def main():
    path, size = create_backup()
    print(f"备份完成: {path}")
    print(f"大小: {size:,} bytes")

if __name__ == '__main__':
    main()
