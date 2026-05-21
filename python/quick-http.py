#!/usr/bin/env python3
import http.server, socketserver, os, sys, argparse

def main():
    parser = argparse.ArgumentParser(description='简易 HTTP 服务器 (开发调试用)')
    parser.add_argument('-p', '--port', type=int, default=8000)
    parser.add_argument('-d', '--dir', default='.')
    parser.add_argument('-b', '--bind', default='0.0.0.0')
    args = parser.parse_args()
    
    os.chdir(args.dir)
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer((args.bind, args.port), handler) as httpd:
        print(f"  HTTP 服务器: http://{args.bind}:{args.port}")
        print(f"  根目录: {os.path.abspath(args.dir)}")
        print(f"  Ctrl+C 停止")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  已停止")

if __name__ == '__main__':
    main()
