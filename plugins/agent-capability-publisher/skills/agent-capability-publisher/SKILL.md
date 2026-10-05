---
name: agent-capability-publisher
description: 将用户描述的可复用工作流整理成生产可用的 Agent Skill，完成校验、打包、人类可读文档、可选的 skills-only Codex Plugin 包装，以及 GitHub 发布或更新。Use when the user asks to create, refine, standardize, package, release, or publish a reusable Skill from requirements, examples, an existing workflow, or an iterative conversation; especially when the endpoint should be a GitHub repository and Codex-installable plugin rather than only a local SKILL.md.
---

# Agent Capability Publisher

把用户已经确认过的真实工作流提炼成可复用的 Agent Skill，并继续完成验证、打包、GitHub 发布和可选的 Codex Plugin 分发。

## 核心原则

- 以用户真实目标、示例、已接受决策和完成标准为准，不重新发明需求。
- 区分 **Skill 行为**、**GitHub 项目展示** 和 **Plugin 分发结构**。
- 保持 `SKILL.md` 精简；条件性细节放 `references/`；脆弱或重复的确定性操作放 `scripts/`。
- 发布前必须验证和测试；不能因为命令“看起来正确”就宣称安装流程已经验证。
- 涉及 ChatGPT / Codex / OpenAI Plugin 时，优先查询当前官方文档，而不是依赖记忆。
- README、Demo 和项目主页只描述最终能力，不写开发日志，除非用户明确要求。
- 默认保留 Git 历史；未经明确授权，不重写历史，不 force-push。

## 工作流

1. **理解需求。**
   - 阅读 `references/requirements-intake.md`。
   - 明确输入、输出、触发请求、连接器/工具、约束和 2–5 个具体示例。
   - 复用当前对话里已经确认的信息，不重复询问已经回答过的问题。

2. **在必要时研究目标生态。**
   - 涉及 ChatGPT / Codex / OpenAI Plugin 时，在决定 manifest、安装命令或发布方式前先核对当前官方文档。
   - 对特定领域的 Skill，仅在确实能改善设计时参考代表性的高质量公开 Skill。
   - 只吸收稳定、与任务直接相关的规范，不复制其他仓库的噪声。

3. **设计 Skill。**
   - 阅读 `references/skill-design.md`。
   - 新 Skill 使用简短的小写连字符命名；除非生态要求，否则不要把 `skill` 放进 Skill 名称。
   - 决定哪些行为放在 `SKILL.md`，哪些细节放在 `references/`，哪些脆弱或重复操作放在 `scripts/`。
   - frontmatter 的 `description` 同时写清“做什么”和“何时触发”。

4. **初始化并实现。**
   - 新 Skill 如果有官方初始化器，优先使用。
   - 交付前删除 placeholder 和示例垃圾文件。
   - 只加入真正提高可靠性或复用性的资源。
   - 新增确定性脚本后必须实际运行测试；如果是一组相似脚本，至少测试代表性路径和高风险分支。

5. **校验并打包 Skill。**
   - 有官方 validator / packager 时优先使用。
   - 用户需要独立 Skill 交付物时，输出完整的 `skill.zip`。
   - `skill.zip` 只保留运行所需的 `SKILL.md`、`agents/`、`scripts/`、`references/`、`assets/`；README、Demo 等 GitHub 展示内容不要塞进 Skill 包。

6. **准备 GitHub 仓库。**
   - 阅读 `references/github-release.md`。
   - README 只覆盖：它是什么、怎么安装/使用、示例、输出、安全和限制。
   - 除非用户明确要求，不把开发过程写进项目主页。
   - 用 `.gitignore` 隔离生成物和临时 render/build job。
   - 不发布 Token、`.env` 值、密码、私钥、Cookie 或连接器凭据。

7. **需要 Codex 安装时包装成 Plugin。**
   - 阅读 `references/codex-plugin-publishing.md`。
   - 优先使用当前 portable 根 `plugin.json` + `skills/` 结构；只有兼容性有价值时才保留 `.codex-plugin/plugin.json`。
   - 使用 `scripts/sync_codex_plugin.py` 把最终 Skill 镜像进 Plugin 包并生成仓库 Marketplace。
   - skills-only Plugin 不需要 MCP Server。
   - 验证 Marketplace 中的 source path 是从 Marketplace 仓库根目录解析的。

8. **通过 GitHub Connector 或 Git 发布。**
   - 优先做连贯提交，不要为了每一行小改动制造独立提交。
   - 用户没有授权创建新仓库、修改可见性、覆盖共享文件、删除历史或 force-push 时，先询问。
   - **新建仓库后，先检查当前 GitHub App/Connector 是否被授权访问该仓库。**
   - 如果 GitHub App 使用 `Selected repositories`，而目标新仓库不在授权列表中，引导用户执行：`GitHub Settings → Applications → Installed GitHub Apps → 当前 App → Configure → Repository access → 添加目标仓库 → Save`。
   - 如果写入返回 `403 Resource not accessible by integration`，优先判断是否为上述仓库授权问题；不要误判成仓库不存在或 API 不支持。
   - 用户完成授权后，重新读取安装可访问仓库列表或重新获取仓库权限，确认目标仓库已经出现，再继续写入。
   - 上传完成后，从 GitHub 重新读回仓库，验证文件、路径、README 链接和 manifest。

9. **验证可安装性。**
   - 有本地 checkout 时，运行 `scripts/check_release.py --repo-root <repo>`。
   - 把 Codex 安装命令写进 README 前，再核对当前官方文档。
   - 对仓库 Marketplace，确认 `.agents/plugins/marketplace.json`、Plugin source path、根 `plugin.json` 和 `skills/<name>/SKILL.md` 全部能正确解析。
   - 条件允许时，在干净的 Codex 会话中实际测试发现/安装，再宣称端到端安装完成。

10. **整理正式发布。**
    - 阅读 `references/release-hygiene.md`。
    - Demo 只展示成品能力；由项目自身生成的 Demo 可以作为能力证明。
    - 发布前删除一次性 TTS/render job、临时 workflow、缓存和 staging 目录，除非它们本来就是可复用基础设施。
    - 默认保留历史。用户如果希望 GitHub 文件列表的“最新提交”统一成正式发布信息，说明可通过触碰这些路径或重写历史实现；重写历史必须再次获得明确授权。

## 决策树

```text
用户要把一个工作流做成可复用能力
├─ 需求/示例不完整
│  └─ 只问关键问题
├─ 更新已有 Skill
│  └─ 保留结构 → 修改 → 校验 → 重新打包
└─ 新建 Skill
   └─ 初始化 → 实现 → 测试 → 校验 → 打包

需要发布到 GitHub？
├─ 否
│  └─ 交付 skill.zip
└─ 是
   ├─ 先确认 GitHub App/Connector 对目标仓库有写权限
   │  └─ Selected repositories 缺少新仓库 → 请求用户授权 → 再继续
   ├─ 只做人类可读仓库
   │  └─ README + Skill 源码 + 发布 QA
   └─ 还要可安装到 Codex
      └─ Skill → Plugin skills/ → Marketplace → 安装验证
```

## 输出约定

当用户要求完整流程时，尽量交付：

- 已校验的 Skill 源码目录；
- 需要独立 Skill 包时的 `skill.zip`；
- 实际测试过的辅助脚本和聚焦的 references；
- README 完整、面向用户的 GitHub 仓库；
- 用户要求时的 skills-only Codex Plugin 包和仓库 Marketplace；
- 基于当前官方文档确认过的安装说明；
- 一份简短发布摘要，明确区分“实际测试通过”和“尚未端到端验证”。

## 约束

- 缺失需求会实质改变 Skill 行为时，不要自行猜测。
- 不要把大段文档堆进 `SKILL.md`。
- README / Demo 不要进入 `skill.zip`，除非运行时确实需要。
- skills-only 工作流不要无意义地创建 MCP Server。
- 未经授权，不创建新的公开仓库、不改可见性、不重写 Git 历史、不 force-push。
- GitHub 写入 403 时，先检查 GitHub App 对新仓库的授权范围。
- 没有真正运行相关 validator / 脚本 / 安装流程，就不要称为“已测试”。

## References

- 需求发现前读取 `references/requirements-intake.md`。
- 新建或大幅调整 Skill 结构前读取 `references/skill-design.md`。
- 需要 Codex 安装/分发时读取 `references/codex-plugin-publishing.md`。
- 创建或更新 GitHub 仓库前读取 `references/github-release.md`。
- 最终清理和交付前读取 `references/release-hygiene.md`。
