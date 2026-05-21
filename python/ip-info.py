#!/usr/bin/env python3
"""IP Info Lookup - IP 地址信息查询 (本地检测)"""
import socket, sys, argparse

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

def get_hostname():
    return socket.gethostname()

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except:
        return None

def main():
    parser = argparse.ArgumentParser(description='IP 信息查询')
    parser.add_argument('hostname', nargs='?', help='要解析的主机名')
    args = parser.parse_args()
    
    print(f"  主机名: {get_hostname()}")
    print(f"  本地 IP: {get_local_ip()}")
    
    if args.hostname:
        ip = resolve_hostname(args.hostname)
        if ip:
            print(f"  {args.hostname} -> {ip}")
        else:
            print(f"  无法解析: {args.hostname}")

if __name__ == '__main__':
    main()
