#!/usr/bin/env python3
"""Port Scanner - 端口占用检查工具"""
import socket, sys

COMMON_PORTS = {
    80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL', 5432: 'PostgreSQL',
    6379: 'Redis', 27017: 'MongoDB', 8080: 'HTTP-Alt', 9090: 'Prometheus',
    3000: 'Grafana', 2181: 'ZooKeeper', 9200: 'Elasticsearch', 5601: 'Kibana',
    5672: 'RabbitMQ', 15672: 'RabbitMQ-UI', 9000: 'MinIO/Portainer',
}

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex(('127.0.0.1', port))
        return result == 0
    except:
        return False
    finally:
        sock.close()

def main():
    if len(sys.argv) > 1:
        try:
            ports = [int(p) for p in sys.argv[1:]]
        except:
            print("用法: python port-checker.py [port1 port2 ...]")
            sys.exit(1)
    else:
        ports = sorted(COMMON_PORTS.keys())
    
    for port in ports:
        name = COMMON_PORTS.get(port, '')
        label = f"{name} ({port})" if name else str(port)
        if check_port(port):
            print(f"  📍 {label:<25} 已占用")
        else:
            print(f"  ✅ {label:<25} 可用")

if __name__ == '__main__':
    main()
