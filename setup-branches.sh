#!/bin/bash

# Script to create four experiment branches for Data Visualization experiments
# 为数据可视化实验创建四个实验分支的脚本

echo "创建实验分支 (Creating experiment branches)..."
echo "================================================"

# Array of branch names
branches=("experiment-1" "experiment-2" "experiment-3" "experiment-4")

# Get current branch
current_branch=$(git branch --show-current)

for branch in "${branches[@]}"; do
    # Check if branch already exists locally
    if git show-ref --verify --quiet "refs/heads/$branch"; then
        echo "✓ 分支 $branch 已存在 (Branch $branch already exists locally)"
    else
        echo "→ 创建分支 $branch (Creating branch $branch)"
        git checkout -b "$branch"
        git checkout "$current_branch"
    fi
    
    # Check if branch exists on remote
    if git ls-remote --heads origin "$branch" | grep -q "$branch"; then
        echo "✓ 远程分支 $branch 已存在 (Remote branch $branch already exists)"
    else
        echo "→ 推送分支 $branch 到远程 (Pushing branch $branch to remote)"
        git push origin "$branch"
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
