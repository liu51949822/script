#!/usr/bin/env python3
"""SSL Certificate Expiry Checker - 批量检查 SSL 证书有效期"""
import ssl, socket, sys, datetime

def get_cert_expiry(hostname, port=443, timeout=5):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    with socket.create_connection((hostname, port), timeout=timeout) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            not_after = cert.get('notAfter', '').strip()
            if not_after:
                return datetime.datetime.strptime(
                    not_after, '%b %d %H:%M:%S %Y %Z'
                ).replace(tzinfo=datetime.timezone.utc)
    return None

def main():
    if len(sys.argv) < 2:
        print("用法: python cert-expiry.py domain1.com [domain2.com ...]")
        print("或: python cert-expiry.py --check google.com github.com docker.com")
        sys.exit(1)
    
    domains = sys.argv[1:] if sys.argv[1] != '--check' else sys.argv[2:]
    
    for domain in domains:
        print(f"  检查: {domain}...", end=' ')
        try:
            expiry = get_cert_expiry(domain)
            if expiry:
                days_left = (expiry - datetime.datetime.now(datetime.timezone.utc)).days
                icon = '⚠️' if days_left < 30 else '✅'
                print(f'{icon} 到期: {expiry.strftime("%Y-%m-%d")} (剩余 {days_left} 天)')
            else:
                print('❌ 无法获取证书')
        except Exception as e:
            print(f'❌ {e}')

if __name__ == '__main__':
    main()
