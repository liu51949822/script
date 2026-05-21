#!/usr/bin/env python3
"""Password Generator - 安全密码生成工具"""
import secrets, string, sys, argparse

def generate(length=16, upper=True, lower=True, digits=True, special=True):
    chars = ''
    if upper: chars += string.ascii_uppercase
    if lower: chars += string.ascii_lowercase
    if digits: chars += string.digits
    if special: chars += '!@#$%^&*()-_=+[]{}'
    
    if not chars:
        return None
    
    password = [
        secrets.choice(string.ascii_uppercase) if upper else '',
        secrets.choice(string.ascii_lowercase) if lower else '',
        secrets.choice(string.digits) if digits else '',
        secrets.choice('!@#$%^&*()-_=+[]{}') if special else '',
    ]
    password = [c for c in password if c]
    remaining = length - len(password)
    password.extend(secrets.choice(chars) for _ in range(remaining))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='安全密码生成器')
    parser.add_argument('-l', '--length', type=int, default=16)
    parser.add_argument('-n', '--count', type=int, default=3)
    parser.add_argument('--no-upper', action='store_true')
    parser.add_argument('--no-lower', action='store_true')
    parser.add_argument('--no-digits', action='store_true')
    parser.add_argument('--no-special', action='store_true')
    args = parser.parse_args()
    
    for i in range(args.count):
        pw = generate(args.length, 
                      not args.no_upper, not args.no_lower,
                      not args.no_digits, not args.no_special)
        if pw:
            strength = '强' if args.length >= 16 else '中' if args.length >= 12 else '弱'
            print(f"  [{strength}] {pw}")
        else:
            print("错误: 至少需要一种字符类型")

if __name__ == '__main__':
    main()
