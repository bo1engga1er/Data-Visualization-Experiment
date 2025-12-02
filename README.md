# Data-Visualization-Experiment
2025hust数据可视化实验

## 实验分支结构 (Experiment Branch Structure)

本仓库包含四个独立的实验分支，每个分支对应一个数据可视化实验：

- `experiment-1`: 第一次实验
- `experiment-2`: 第二次实验
- `experiment-3`: 第三次实验
- `experiment-4`: 第四次实验

### 初始化设置 (Initial Setup)

实验分支已在本地创建。要推送到远程仓库，请使用：

```bash
# 推送所有实验分支
./push-branches.sh
```

或者使用 GitHub Actions 工作流（在 Actions 标签页中手动触发 "Create Experiment Branches" 工作流）。

详细的设置说明请参见 [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)。

### 使用说明 (Usage Instructions)

切换到特定的实验分支进行开发：

```bash
# 切换到实验1
git checkout experiment-1

# 切换到实验2
git checkout experiment-2

# 切换到实验3
git checkout experiment-3

# 切换到实验4
git checkout experiment-4
```

每个实验分支将包含该实验的独立代码和资源。
