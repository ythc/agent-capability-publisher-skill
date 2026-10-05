# GitHub 发布流程

## 仓库应该包含什么

一个整理良好的 Skill 仓库通常需要：

- 用户偏好语言的简洁 README；
- canonical Skill 源码；
- 可选的 Codex Plugin / Marketplace 结构；
- 用于生成物的 `.gitignore`；
- 用户选择后的 License；
- 能证明最终能力的可选 Demo。

## README 顺序

推荐：一句话定位 → Demo/结果证明 → 安装 → 使用示例 → 能力和输出 → 必要的结构说明 → 更新方式 → 安全/限制。

除非用户明确要 changelog 或工程记录，否则不要在项目主页讲开发过程。

## GitHub Connector 写入前检查

使用 GitHub Connector / GitHub App 发布前，先确认它对目标仓库有写权限。

如果 GitHub App 的 Repository access 是 **Selected repositories**，用户刚创建的新仓库通常不会自动加入授权范围。先检查当前 App 能访问的仓库列表；若目标仓库不在其中，引导用户执行：

```text
GitHub
→ Settings
→ Applications
→ Installed GitHub Apps
→ 当前 GitHub App
→ Configure
→ Repository access
→ Selected repositories
→ 添加目标新仓库
→ Save
```

如果能拿到当前安装页面，也可以提供：

```text
https://github.com/settings/installations/<installation_id>
```

用户授权完成后，再次读取该 App 可访问的仓库列表，确认目标仓库已经出现，再继续写入。

如果仓库存在、账号也有管理权限，但写入返回：

```text
403 Resource not accessible by integration
```

优先检查 GitHub App 是否没有被授权到这个新仓库，不要立刻判断成仓库不存在、API 不支持写入或用户没有仓库权限。

## GitHub 操作顺序

1. 检查目标仓库和连接权限；
2. 新仓库先确认 GitHub App 授权范围；
3. 写之前读取当前文件；
4. 做连贯更新；
5. 写完后从 GitHub 重新读取 tree / README / manifest；
6. 默认保留提交历史。

修改可见性、删除 branch/tag/release、force-push、重写历史或删除非临时用户内容前，先获得明确授权。

## Demo 和清理

由能力本身生成的 Demo 很有价值。把它描述成最终产物示例，而不是开发过程故事。

发布前清理 `.codebase-video/`、`render-jobs/current/`、`tts-jobs/current/`、`node_modules/`、`out/`、`__pycache__/` 等临时路径；可复用基础设施除外。
