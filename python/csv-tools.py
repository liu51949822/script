#!/usr/bin/env python3
"""CSV ↔ JSON 互转工具 — 双向转换支持自定义分隔符
用法: python csv-tools.py data.csv              # CSV → JSON
      python csv-tools.py data.json -r           # JSON → CSV
      python csv-tools.py data.csv -d ';'        # 指定分隔符"""
import csv, json, sys, argparse, io

def csv_to_json(input_file, output_file=None, delimiter=','):
    with open(input_file, newline='') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        data = list(reader)
    
    output = output_file or input_file.rsplit('.', 1)[0] + '.json'
    with open(output, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"CSV -> JSON: {output} ({len(data)} 行)")

def json_to_csv(input_file, output_file=None, delimiter=','):
    with open(input_file) as f:
        data = json.load(f)
    
    if not data:
        print("JSON 为空")
        return
    
    output = output_file or input_file.rsplit('.', 1)[0] + '.csv'
    with open(output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
    print(f"JSON -> CSV: {output} ({len(data)} 行)")

def main():
    parser = argparse.ArgumentParser(description='CSV <-> JSON 转换工具')
    parser.add_argument('input', help='输入文件')
    parser.add_argument('-o', '--output', help='输出文件')
    parser.add_argument('-d', '--delimiter', default=',', help='CSV 分隔符')
    parser.add_argument('-r', '--reverse', action='store_true', help='JSON -> CSV')
    args = parser.parse_args()
    
    if args.reverse:
        json_to_csv(args.input, args.output, args.delimiter)
    else:
        csv_to_json(args.input, args.output, args.delimiter)

if __name__ == '__main__':
    main()
