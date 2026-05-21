#!/usr/bin/env python3
"""Docker Stats Analyzer - 容器资源使用分析"""
import subprocess, json, sys, argparse

def get_container_stats():
    result = subprocess.run(
        ['docker', 'stats', '--no-stream', '--format', '{{json .}}'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return []
    stats = []
    for line in result.stdout.strip().split('\n'):
        if line:
            try:
                stats.append(json.loads(line))
            except:
                pass
    return stats

def parse_memory(mem_str):
    if not mem_str or mem_str == '0B':
        return 0
    mem_str = mem_str.split('/')[0].strip()
    units = {'B': 1, 'KiB': 1024, 'MiB': 1024**2, 'GiB': 1024**3}
    for unit, multiplier in units.items():
        if unit in mem_str:
            return float(mem_str.replace(unit, '')) * multiplier
    return 0

def parse_cpu(cpu_str):
    return float(cpu_str.replace('%', '')) if cpu_str else 0

def main():
    parser = argparse.ArgumentParser(description='容器资源分析')
    parser.add_argument('--top', type=int, default=10, help='显示前 N 个')
    args = parser.parse_args()
    
    stats = get_container_stats()
    if not stats:
        print("没有运行中的容器")
        return
    
    data = []
    for s in stats:
        name = s.get('Name', '')
        cpu = parse_cpu(s.get('CPUPerc', '0%'))
        mem = parse_memory(s.get('MemUsage', '0B'))
        data.append((name, cpu, mem))
    
    data.sort(key=lambda x: x[2], reverse=True)
    
    print(f"{'容器':<25} {'CPU %':>8} {'内存':>12}")
    print('-' * 50)
    for name, cpu, mem in data[:args.top]:
        print(f"  {name:<23} {cpu:>7.1f}% {mem/1024/1024:>9.1f} MiB")

if __name__ == '__main__':
    main()
