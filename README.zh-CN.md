# Agent Capability Publisher

[English](README.md) | **简体中文**

**Agent Capability Publisher** 是一个可安装到 Codex 的 Plugin，里面包含一个 Agent Skill，用来把“需求或反复打磨出来的工作流”整理成生产可用的 Skill，并完成校验、打包、GitHub 项目整理和 Codex Plugin 分发准备。

你可以直接把需求、示例、现有工作流，或者一段已经迭代多轮的聊天交给 Codex。这个 Skill 会提炼最终规范、设计 Skill 结构、测试确定性脚本、生成 `skill.zip`、整理面向用户的 README，并在需要时把 Skill 包装成可安装到 Codex 的 skills-only Plugin。

## 安装到 Codex

把这个 GitHub 仓库加入 Plugin Marketplace：

```bash
codex plugin marketplace add ythc/agent-capability-publisher-skill --ref main
```

然后启动 Codex：

```bash
codex
```

输入：

```text
/plugins
```

找到 **Agent Capability Publisher**，选择 **Install plugin**，安装后新建一个 Codex 会话。

## 使用

例如：

```text
把这个工作流做成一个可复用的 Agent Skill，完成校验、打包，并准备好 GitHub 和 Codex 的发布结构。
```

```text
我们已经来回讨论了很多轮。提取最终需求，创建 Skill，测试通过后打包；README 只写最终产品，不要把开发过程写进去。
```

```text
更新这个现有 Skill，保留原有结构，重新校验并生成 Codex Plugin 和 GitHub 发布内容。
```

## 能做什么

- **理解需求**：从目标、输入输出、触发示例、约束、已接受决策和完成标准中提炼稳定规范。
- **设计 Skill**：让 `SKILL.md` 保持精简，把细节放到 `references/`，把确定性操作放进经过实际测试的 `scripts/`。
- **校验和打包**：优先使用目标平台官方 validator / packager，并在需要时生成完整 `skill.zip`。
- **Codex Plugin 包装**：把最终 Skill 镜像到 skills-only Plugin，生成 portable `plugin.json`、兼容 manifest 和仓库 Marketplace。
- **GitHub 项目整理**：生成面向用户的 README、安装说明、使用示例和发布清理规则，而不是开发日志。
- **发布验证**：检查 manifest、Marketplace 路径、临时文件和实际测试状态，避免把“语法正确”误报成“真实安装已验证”。

## Plugin 结构

```text
.agents/plugins/marketplace.json

plugins/agent-capability-publisher/
├── plugin.json
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── agent-capability-publisher/
        ├── SKILL.md
        ├── agents/
        ├── scripts/
        └── references/
```

可安装的 Skill 源码直接位于 `plugins/agent-capability-publisher/skills/agent-capability-publisher/`。README 等 GitHub 展示内容不会进入 Skill 运行时包。

## 更新

```bash
codex plugin marketplace upgrade agent-capability-publisher
```

更新后新建一个 Codex 会话。

## 安全和发布规则

未经明确授权，这个 Skill 不会重写 Git 历史、force-push、修改仓库可见性，也不会发布敏感凭据。它会把本地校验、脚本测试、GitHub 上传和 Codex 端到端安装验证区分开，准确说明哪些步骤真正执行过。
