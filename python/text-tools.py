#!/usr/bin/env python3
import sys, random, string, hashlib, base64, textwrap, argparse

def gen_uuid(): return f"{random.randint(0,0xffffffff):08x}-{random.randint(0,0xffff):04x}-{random.randint(0,0xffff):04x}-{random.randint(0,0xffff):04x}-{random.randint(0,0xffffffffffff):012x}"

def gen_base64(text): return base64.b64encode(text.encode()).decode()
def decode_base64(text): return base64.b64decode(text).decode()

def gen_hash(text, algo='sha256'): return hashlib.new(algo, text.encode()).hexdigest()

def count_chars(text):
    return len(text), len(text.encode('utf-8'))

def case_convert(text, mode):
    if mode == 'upper': return text.upper()
    if mode == 'lower': return text.lower()
    if mode == 'title': return text.title()
    if mode == 'snake': return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text

TOOLS = {
    'uuid': lambda _: gen_uuid(),
    'b64enc': lambda t: gen_base64(t),
    'b64dec': lambda t: decode_base64(t),
    'md5': lambda t: gen_hash(t, 'md5'),
    'sha256': lambda t: gen_hash(t, 'sha256'),
    'upper': lambda t: case_convert(t, 'upper'),
    'lower': lambda t: case_convert(t, 'lower'),
    'snake': lambda t: case_convert(t, 'snake'),
    'count': lambda t: f"{count_chars(t)[0]} 字符 / {count_chars(t)[1]} bytes",
}

def main():
    parser = argparse.ArgumentParser(description='开发常用文本工具')
    parser.add_argument('tool', choices=list(TOOLS.keys()), help='工具名')
    parser.add_argument('text', nargs='?', help='输入文本')
    args = parser.parse_args()
    
    if args.text:
        print(TOOLS[args.tool](args.text))
    else:
        text = sys.stdin.read().strip()
        print(TOOLS[args.tool](text))

if __name__ == '__main__':
    main()
