# 实验分支设置说明 (Experiment Branch Setup Instructions)

本文档说明如何为四个数据可视化实验创建和推送分支。

## 方法一：使用设置脚本（推荐）

已经创建了四个本地实验分支，每个分支都包含初始的 `EXPERIMENT.md` 文件。要将这些分支推送到远程仓库：

```bash
# 推送所有实验分支到远程
git push origin experiment-1
git push origin experiment-2
git push origin experiment-3
git push origin experiment-4
```

或者运行自动化脚本：

```bash
./setup-branches.sh
```

## 方法二：使用 GitHub Actions（自动化）

1. 进入仓库的 GitHub 页面
2. 点击 "Actions" 标签页
3. 选择 "Create Experiment Branches" 工作流
4. 点击 "Run workflow" 按钮
5. 等待工作流完成，四个分支将自动创建并推送

## 方法三：手动创建（如果需要）

如果本地分支不存在，可以手动创建：

```bash
# 为每个实验创建分支
for i in {1..4}; do
  git checkout -b "experiment-$i"
  
  # 创建实验说明文件
  cat > EXPERIMENT.md << EOF
# 实验${i} (Experiment ${i})

本分支用于第${i}次数据可视化实验。

## 说明
请在本分支进行实验${i}相关的开发工作。
EOF
  
  git add EXPERIMENT.md
  git commit -m "Initialize experiment-${i} branch"
  git push -u origin "experiment-$i"
  
  # 返回主分支
  git checkout -
done
```

## 验证分支创建

查看所有分支（包括远程）：

```bash
git branch -a
```

应该看到：
- `experiment-1`
- `experiment-2`
- `experiment-3`
- `experiment-4`

## 使用实验分支

切换到特定的实验分支进行开发：

```bash
# 切换到实验 1
git checkout experiment-1

# 切换到实验 2
git checkout experiment-2

# 切换到实验 3
git checkout experiment-3

# 切换到实验 4
git checkout experiment-4
```

## 注意事项

- 每个实验分支是独立的，可以包含不同的代码和资源
- 在实验分支上进行开发时，记得定期提交并推送更改
- 如果需要合并实验成果，可以使用 Pull Request 或 merge 命令
