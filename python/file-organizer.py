#!/usr/bin/env python3
"""
文件整理工具 - 按类型自动归类文件到子目录
用法: python file-organizer.py [目标目录] [--dry-run]

分类规则:
  - 图片: jpg, png, gif, webp, svg, bmp, ico
  - 文档: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, md
  - 压缩包: zip, rar, 7z, tar, gz, bz2
  - 代码: py, js, ts, html, css, java, go, rs, sh, bat, ps1
  - 视频: mp4, avi, mkv, mov, wmv, flv
  - 音频: mp3, wav, flac, ogg, aac, m4a
"""

import os
import shutil
import sys
from pathlib import Path

FILE_CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico"},
    "documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md", ".csv"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "code": {".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".scss", ".java", ".go", ".rs", ".sh", ".bat", ".ps1", ".yaml", ".yml", ".json", ".xml"},
    "videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"},
    "audio": {".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".wma"},
}

def organize_directory(target_dir: str, dry_run: bool = False):
    target = Path(target_dir).resolve()
    if not target.is_dir():
        print(f"❌ 目录不存在: {target}")
        return

    print(f"{'🔄 模拟运行' if dry_run else '📦 开始整理'} - {target}")
    stats = {cat: 0 for cat in FILE_CATEGORIES}
    stats["unknown"] = 0

    for item in target.iterdir():
        if item.is_file() and not item.name.startswith("."):
            ext = item.suffix.lower()
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    dest_dir = target / category
                    if not dry_run:
                        dest_dir.mkdir(exist_ok=True)
                        shutil.move(str(item), str(dest_dir / item.name))
                    stats[category] += 1
                    print(f"  {category}/ <- {item.name}")
                    moved = True
                    break
            if not moved:
                stats["unknown"] += 1

    print(f"\n📊 统计:")
    for cat, count in stats.items():
        if count > 0:
            print(f"  {cat}: {count} 个文件")

if __name__ == "__main__":
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    target = [a for a in args if not a.startswith("--")]
    organize_directory(target[0] if target else ".", dry_run)
