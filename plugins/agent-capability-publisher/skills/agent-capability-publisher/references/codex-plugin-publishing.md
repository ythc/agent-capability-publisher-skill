# Codex Plugin 分发

## 原则

当用户希望 Skill 可以在 Codex 里安装和发现时，把最终 Skill 包装成 skills-only Plugin，而不是只交付一个 `skill.zip`。

发布前重新核对当前 OpenAI 官方 Plugin / Codex 文档，避免把某一时期的安装命令或 manifest 结构永久写死。

## 推荐结构

```text
.agents/plugins/marketplace.json

plugins/<plugin-name>/
├── plugin.json
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── <skill-name>/
        ├── SKILL.md
        ├── agents/
        ├── scripts/
        ├── references/
        └── assets/
```

skills-only Plugin 不需要为了“像 Plugin”而额外创建 MCP Server。

## Portable manifest

优先使用当前 portable 根 `plugin.json`。Plugin 标识、版本、展示名、描述和 Skill 目录要互相一致。`shortDescription` 保持足够短，并在打包前实际检查平台长度限制。

## Marketplace

仓库 Marketplace 放在 `.agents/plugins/marketplace.json`。其中本地 source path 按 Marketplace 仓库根目录解析，例如：

```json
{
  "source": {
    "source": "local",
    "path": "./plugins/my-plugin"
  }
}
```

不要误以为它是相对于 `.agents/plugins/` 解析。

## 安装验证

把 Codex 安装命令写入 README 前，查询当前官方文档并确认实际语法。结构校验通过不等于端到端安装已验证。

能运行 Codex CLI 时，尽量真实测试：添加 Marketplace → 确认列表可见 → 进入 `/plugins` → 安装 Plugin → 新建会话 → 用典型请求验证 Skill 能被发现和触发。

无法运行 Codex CLI 时，要明确写“结构和 manifest 已验证，但端到端安装尚未在当前环境实际测试”。
