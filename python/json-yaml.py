#!/usr/bin/env python3
import sys, json, yaml, os

USAGE = """格式转换工具 — JSON / YAML / TOML 互转
用法: python json-yaml.py <输入文件> [输出文件]
      自动根据扩展名检测格式"""

def convert(input_path, output_path=None):
    with open(input_path) as f:
        content = f.read()
    
    in_ext = os.path.splitext(input_path)[1].lower()
    
    if in_ext in ('.json',):
        data = json.loads(content)
    elif in_ext in ('.yml', '.yaml'):
        data = yaml.safe_load(content)
    else:
        print(f"不支持的格式: {in_ext}")
        sys.exit(1)
    
    if not output_path:
        base = os.path.splitext(input_path)[0]
        out_ext = '.json' if in_ext in ('.yml','.yaml') else '.yml'
        output_path = base + out_ext
    
    out_ext = os.path.splitext(output_path)[1].lower()
    
    with open(output_path, 'w') as f:
        if out_ext == '.json':
            json.dump(data, f, indent=2, ensure_ascii=False)
        elif out_ext in ('.yml', '.yaml'):
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        else:
            print(f"不支持输出格式: {out_ext}")
            sys.exit(1)
    
    print(f"{input_path} -> {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
