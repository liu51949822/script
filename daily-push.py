#!/usr/bin/env python3
"""
每日脚本推送工具
每天 7:00-8:00 执行，生成新的脚本/技能并推送到 GitHub

用法: python daily-push.py
配置: 设置 GITHUB_TOKEN 环境变量
"""

import os
import sys
import subprocess
import random
from datetime import date, datetime
from pathlib import Path

REPO_DIR = Path(r"E:\openclaw\script-repo")
MAX_FILES = 5

# ===== 今天的生成内容 =====
# 每天从以下模板池中随机挑选，也可以写新代码
# 格式: (category, filename, content_generator)

TODAY = date.today()

def docker_compose(name, desc, port, image, extra=""):
    return f"""# {name} - {desc}
#
# 安装: docker compose up -d
# 访问: http://localhost:{port}
# 生成日期: {TODAY}

services:
  {name}:
    image: {image}
    container_name: {name}
    ports:
      - "{port}:{port}"
    volumes:
      - ./data:/data
    restart: unless-stopped
{extra}
"""

def shell_script(name, desc, commands):
    return f"""#!/bin/bash
# {name} - {desc}
# 生成日期: {TODAY}

set -e

echo "=== {name} ==="
{commands}
echo "=== 完成 ==="
"""

def python_script(name, desc, code):
    return f'''#!/usr/bin/env python3
"""
{name} - {desc}
生成日期: {TODAY}
"""

import os
import sys
from pathlib import Path

{code}

if __name__ == "__main__":
    main()
'''


# 每日内容池 ── 可每天随机选，也可以定期轮换
CONTENT_POOL = [
    # ── Docker compose 新服务 ──
    {
        "path": "docker/suitecrm/installcompose.file",
        "content": docker_compose("suitecrm", "开源 CRM 客户管理系统", "8080", "bitnami/suitecrm:latest"),
        "msg": "add SuiteCRM docker compose - open source CRM",
    },
    {
        "path": "docker/opengist/installcompose.file",
        "content": docker_compose("opengist", "轻量 Git Snippets", "6150", "ghcr.io/thomiceli/opengist:latest"),
        "msg": "add Opengist docker compose - Git snippets",
    },
    {
        "path": "docker/listmonk/installcompose.file",
        "content": docker_compose("listmonk", "开源邮件营销平台", "9000", "listmonk/listmonk:latest"),
        "msg": "add Listmonk docker compose - email marketing",
    },
    {
        "path": "docker/docmost/installcompose.file",
        "content": docker_compose("docmost", "开源文档协作平台", "8080", "docmost/docmost:latest"),
        "msg": "add Docmost docker compose - documentation",
    },
    {
        "path": "docker/mailpit/installcompose.file",
        "content": docker_compose("mailpit", "开发邮件测试工具", "8025", "axllent/mailpit:latest"),
        "msg": "add Mailpit docker compose - dev email testing",
    },
    # ── Shell 脚本 ──
    {
        "path": "base/disk-cleanup.sh",
        "content": shell_script("磁盘清理", "清理临时文件和缓存释放空间",
            '''echo "  清理 Docker 无用数据..."
docker system prune -af --volumes 2>/dev/null && echo "  done" || echo "  docker not available"
echo "  清理临时文件..."
rm -rf /tmp/* 2>/dev/null
rm -rf ~/.cache/* 2>/dev/null
echo "  磁盘使用:"
df -h / 2>/dev/null || true'''),
        "msg": "add disk-cleanup script",
    },
    {
        "path": "base/log-rotator.sh",
        "content": shell_script("日志轮转", "自动切割和压缩日志文件",
            '''LOG_DIR="${1:-/var/log}"
DAYS="${2:-7}"
find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -exec gzip {} \\;
find "$LOG_DIR" -name "*.gz" -type f -mtime +30 -delete
echo "  Log rotation completed for $LOG_DIR"'''),
        "msg": "add log-rotator script",
    },
    {
        "path": "base/docker-stats-dashboard.sh",
        "content": shell_script("Docker 统计面板", "Web 可视化 Docker 容器状态",
            '''echo "<html><body><h1>Docker Stats</h1><pre>$(docker stats --no-stream 2>&1)</pre></body></html>" > /tmp/docker-stats.html
echo "  Dashboard: file:///tmp/docker-stats.html"'''),
        "msg": "add docker-stats-dashboard script",
    },
    # ── Python 脚本 ──
    {
        "path": "python/network-score.py",
        "content": python_script("网络评分", "测试网络质量并评分",
            '''import subprocess, json, time

def ping_test(host="8.8.8.8", count=4):
    cmd = ["ping", "-n", str(count), host]
    r = subprocess.run(cmd, capture_output=True, text=True)
    times = []
    for line in r.stdout.split("\\n"):
        if "time=" in line.lower() or "ms" in line.lower():
            parts = line.split()
            for p in parts:
                if "ms" in p:
                    try:
                        t = p.replace("ms", "").replace("time=", "")
                        times.append(float(t))
                    except: pass
    return {"avg": sum(times)/len(times) if times else 0, "packet_loss": 100 - len(times)*25}

def main():
    result = ping_test()
    score = 100
    if result["avg"] > 200: score -= 30
    elif result["avg"] > 100: score -= 15
    elif result["avg"] > 50: score -= 5
    if result["packet_loss"] > 0: score -= result["packet_loss"]
    print(json.dumps({"score": max(0, score), "avg_ms": result["avg"], "loss_pct": result["packet_loss"]}, indent=2))

if __name__ == "__main__":
    main()'''),
        "msg": "add network-score python script",
    },
    {
        "path": "python/dir-diff.py",
        "content": python_script("目录对比", "递归对比两个目录差异",
            '''import os, hashlib, sys

def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_dir(root):
    result = {}
    for dirpath, _, files in os.walk(root):
        for f in files:
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, root)
            result[rel] = file_hash(full)
    return result

def main():
    if len(sys.argv) < 3:
        print("用法: python dir-diff.py <目录A> <目录B>")
        return
    a, b = sys.argv[1], sys.argv[2]
    fa, fb = scan_dir(a), scan_dir(b)
    only_a = set(fa) - set(fb)
    only_b = set(fb) - set(fa)
    diff = {k for k in fa if k in fb and fa[k] != fb[k]}
    print(f"仅在 {a}: {len(only_a)} 文件")
    for f in sorted(only_a)[:10]: print(f"  - {f}")
    print(f"仅在 {b}: {len(only_b)} 文件")
    for f in sorted(only_b)[:10]: print(f"  - {f}")
    print(f"内容不同: {len(diff)} 文件")
    for f in sorted(diff)[:10]: print(f"  ~ {f}")

if __name__ == "__main__":
    main()'''),
        "msg": "add dir-diff python script",
    },
    {
        "path": "python/sys-report.py",
        "content": python_script("系统报告", "生成详细的系统信息报告",
            '''import platform, os, json, subprocess, shutil
from datetime import datetime

def run_cmd(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=5)
        return r.stdout.strip()
    except: return "N/A"

def main():
    report = {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "cpu_count": os.cpu_count(),
        "python": platform.python_version(),
        "timestamp": datetime.now().isoformat(),
        "disk_usage": {},
    }
    if platform.system() == "Windows":
        report["windows_version"] = platform.version()
        for d in "CDEF":
            usage = shutil.disk_usage(f"{d}:\\\\") if os.path.exists(f"{d}:\\\\") else None
            if usage:
                report["disk_usage"][d] = {
                    "total_gb": round(usage.total / 1e9, 1),
                    "used_gb": round(usage.used / 1e9, 1),
                    "free_gb": round(usage.free / 1e9, 1),
                    "pct": round(usage.used / usage.total * 100, 1),
                }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()'''),
        "msg": "add sys-report python script",
    },
]


def push_to_github(token, p):
    """提交并推送到 GitHub (使用 SSH key)"""
    os.chdir(REPO_DIR)

    # 使用 SSH key (公司网络屏蔽 HTTPS)
    subprocess.run(["git", "remote", "set-url", "origin",
                    "git@github.com:liu51949822/script.git"],
                   cwd=REPO_DIR, capture_output=True)

    # Windows 下 Path.home() 返回 Posix 风格路径，必须用正斜杠
    ssh_key = Path.home().as_posix() + "/.ssh/script_repo_key"
    env = os.environ.copy()
    env["GIT_SSH_COMMAND"] = f"ssh -i {ssh_key} -o StrictHostKeyChecking=no"

    # 先拉取远端最新代码 (自动 stash 未提交的改动)
    r = subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"],
                       cwd=REPO_DIR, capture_output=True, env=env, timeout=30)
    if r.returncode != 0:
        p(f"git pull 警告: {r.stderr.decode()}")

    # 提交
    r = subprocess.run(["git", "add", "-A"], cwd=REPO_DIR, capture_output=True, env=env)
    if r.returncode != 0:
        p(f"git add 失败: {r.stderr.decode()}")
        return False

    r = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_DIR, capture_output=True, env=env)
    if r.returncode == 0:
        p("没有新内容需要提交")
        return True

    commit_msg = f"daily push {TODAY}"
    r = subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_DIR, capture_output=True, env=env)
    if r.returncode != 0:
        p(f"git commit 失败: {r.stderr.decode()}")
        return False

    r = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, env=env)
    if r.returncode != 0:
        p(f"git push 失败: {r.stderr.decode()}")
        return False

    p(f"✅ 成功推送至 GitHub: {commit_msg}")
    return True


def main():
    import sys
    # 重定向输出到文件确保能看到
    logfile = Path(__file__).parent / "push-output.log"
    with open(logfile, "a", encoding="utf-8") as log:
        def p(msg):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
            log.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
            log.flush()
        sys.stdout = log
        sys.stderr = log
        _main(p)

def _main(p):
    p(f"📅 每日推送 - {TODAY}")
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        try:
            import json as _json
            cfg_path = Path.home() / ".openclaw" / "openclaw.json"
            if cfg_path.exists():
                cfg = _json.loads(cfg_path.read_text(encoding="utf-8"))
                token = cfg.get("env", {}).get("GITHUB_TOKEN", "")
        except Exception:
            pass

    # 选择今天要生成的内容 (随机选 <= MAX_FILES 个)
    selected = random.sample(CONTENT_POOL, min(MAX_FILES, len(CONTENT_POOL)))

    created = []
    for item in selected:
        filepath = REPO_DIR / item["path"]
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(item["content"], encoding="utf-8")
        created.append(item["path"])
        p(f"  📝 创建: {item['path']}")

    if not token:
        p("")
        p("⚠️  未设置 GITHUB_TOKEN，文件已生成但未推送")
        p(f"   已创建 {len(created)} 个文件:")
        for f in created:
            p(f"    - {f}")
        p("")
        p("   设置环境变量后重新运行即可推送:")
        p("   $env:GITHUB_TOKEN=\"your_token\"")
        p("   python daily-push.py")
        return

    p("")
    p("  📤 推送到 GitHub...")
    push_to_github(token, p)


if __name__ == "__main__":
    main()
