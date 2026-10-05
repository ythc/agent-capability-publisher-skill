# Skill 设计规范

## 分层

把内容分成三层：

1. **SKILL.md**：控制流程、关键约束、决策树、何时读取其他资源。
2. **references/**：条件性细节、平台规范、工作流说明、长文档。
3. **scripts/**：需要稳定、可重复执行的确定性操作。

## SKILL.md

- frontmatter 保持简洁，只放平台允许的字段；
- `name` 使用小写连字符；
- `description` 同时覆盖能力和触发条件；
- 正文尽量短，像控制平面，不像知识库；
- 优先写动作、决策和约束，而不是背景知识；
- 超过约 500 行时继续拆分。

## References

适合放平台规范、复杂发布流程、输出格式、QA 清单和条件分支说明。长 reference 建议加目录；尽量让 `SKILL.md` 直接链接，不做多层嵌套跳转。

## Scripts

只有当脚本能提高正确性、稳定性或重复利用价值时才加入。新增脚本后：先运行 `--help` 或最小调用，再执行代表性输入，验证输出和失败分支，并删除 placeholder。

## Skill 与项目展示分离

- Skill 运行时包只包含需要的 `SKILL.md`、`agents/`、`scripts/`、`references/`、`assets/`。
- README、Demo 视频、宣传图片和 GitHub 页面文档属于仓库展示层，不默认进入 Skill 包。
- 如果还要做 Codex Plugin，把 Skill 镜像进 `plugins/<plugin>/skills/<skill>/`，而不是让 README 充当运行说明。
