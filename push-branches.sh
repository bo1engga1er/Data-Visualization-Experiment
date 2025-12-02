#!/bin/bash

# Simple script to push all experiment branches to remote
# 将所有实验分支推送到远程的简单脚本

echo "推送实验分支到远程 (Pushing experiment branches to remote)..."
echo "================================================"

branches=("experiment-1" "experiment-2" "experiment-3" "experiment-4")

for branch in "${branches[@]}"; do
    if git show-ref --verify --quiet "refs/heads/$branch"; then
        echo "→ 推送 $branch (Pushing $branch)..."
        if git push origin "$branch" 2>&1; then
            echo "✓ $branch 推送成功 (Successfully pushed $branch)"
        else
            echo "✗ $branch 推送失败 (Failed to push $branch)"
        fi
    else
        echo "⚠ 本地分支 $branch 不存在 (Local branch $branch does not exist)"
    fi
    echo ""
done

echo "================================================"
echo "完成！(Done!)"
echo ""
echo "验证远程分支 (Verify remote branches):"
echo "git branch -r | grep experiment"
