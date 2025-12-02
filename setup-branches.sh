#!/bin/bash

# Script to create and push four experiment branches for Data Visualization experiments
# 为数据可视化实验创建并推送四个实验分支的脚本

echo "创建并推送实验分支 (Creating and pushing experiment branches)..."
echo "================================================"

# Array of branch names
branches=("experiment-1" "experiment-2" "experiment-3" "experiment-4")

# Fetch latest from remote
echo "→ 获取远程分支信息 (Fetching remote branches)..."
git fetch origin

for branch in "${branches[@]}"; do
    # Check if branch exists on remote
    if git ls-remote --heads origin "$branch" | grep -q "$branch"; then
        echo "✓ 远程分支 $branch 已存在 (Remote branch $branch already exists)"
        
        # Check if local branch exists
        if git show-ref --verify --quiet "refs/heads/$branch"; then
            echo "  本地分支 $branch 已存在 (Local branch $branch exists)"
        else
            echo "  → 检出远程分支 $branch (Checking out remote branch $branch)"
            git checkout -b "$branch" "origin/$branch"
            git checkout -
        fi
    else
        # Branch doesn't exist on remote
        if git show-ref --verify --quiet "refs/heads/$branch"; then
            echo "→ 推送本地分支 $branch 到远程 (Pushing local branch $branch to remote)"
            git push -u origin "$branch"
        else
            echo "→ 创建并推送分支 $branch (Creating and pushing branch $branch)"
            git checkout -b "$branch"
            git push -u origin "$branch"
            git checkout -
        fi
    fi
done

echo "================================================"
echo "✓ 完成！所有实验分支已创建 (Done! All experiment branches created)"
echo ""
echo "使用以下命令切换到实验分支："
echo "Use the following commands to switch to experiment branches:"
echo ""
echo "  git checkout experiment-1  # 第一次实验"
echo "  git checkout experiment-2  # 第二次实验"
echo "  git checkout experiment-3  # 第三次实验"
echo "  git checkout experiment-4  # 第四次实验"
