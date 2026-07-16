@echo off
REM 每日脚本推送 - Windows 计划任务批次
REM 每日 7:00-8:00 由 Task Scheduler 调用

set REPO_DIR=E:\openclaw\script-repo

cd /d %REPO_DIR%

REM 设置 git 环境
set GIT_SSH_COMMAND=ssh -i %USERPROFILE%\.ssh\script_repo_key -o StrictHostKeyChecking=no

REM 签发 key 权限
icacls "%USERPROFILE%\.ssh\script_repo_key" /inheritance:r /grant "%USERNAME%:R" >nul 2>&1

REM 拉取最新
git pull --rebase origin main 2>nul

REM 生成推送脚本
python daily-push.py

REM 如果 GITHUB_TOKEN 已配置，自动推送
if not "%GITHUB_TOKEN%"=="" (
    echo GITHUB_TOKEN 已配置，尝试推送...
)
