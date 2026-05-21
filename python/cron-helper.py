#!/usr/bin/env python3
"""Cron 表达式工具 — 解析、验证、列出常用 Cron 表达式示例
用法: python cron-helper.py "*/5 * * * *"
      python cron-helper.py -l              # 列出所有常用示例"""
import argparse, datetime

CRON_FIELDS = ['分钟', '小时', '日', '月', '星期']

EXAMPLES = {
    '每分钟': '* * * * *',
    '每小时': '0 * * * *',
    '每天0点': '0 0 * * *',
    '每周一0点': '0 0 * * 1',
    '每月1号0点': '0 0 1 * *',
    '每5分钟': '*/5 * * * *',
    '工作日9点': '0 9 * * 1-5',
    '每隔1小时': '0 */1 * * *',
}

def next_runs(expression, count=5):
    from datetime import datetime, timedelta
    now = datetime.now()
    runs = []
    for i in range(count):
        runs.append(now + timedelta(minutes=i*60))
    return runs

def main():
    parser = argparse.ArgumentParser(description='Cron 表达式工具')
    parser.add_argument('expr', nargs='?', help='Cron 表达式 (如 "*/5 * * * *")')
    parser.add_argument('-l', '--list', action='store_true', help='列出常用示例')
    args = parser.parse_args()
    
    if args.list or not args.expr:
        print("常用 Cron 表达式:\n")
        for desc, expr in EXAMPLES.items():
            print(f"  {expr:<15} {desc}")
        print("\n字段说明: 分钟 小时 日 月 星期")
        return
    
    parts = args.expr.split()
    if len(parts) != 5:
        print("错误: Cron 需要 5 个字段")
        sys.exit(1)
    
    print(f"Cron: {args.expr}")
    print(f"解读: 分钟={parts[0]}, 小时={parts[1]}, 日={parts[2]}, 月={parts[3]}, 星期={parts[4]}")

if __name__ == '__main__':
    import sys
    main()
