# 正式发布清理

## README 和 Demo

- README 只描述最终能力、安装、使用、输出和限制。
- 不写“之前怎么失败、后来怎么修”的过程，除非用户明确需要 changelog 或工程复盘。
- 自生成 Demo 可以保留，并明确说明它是该能力自身生成的成品示例。

## Git 历史

默认保留历史。

如果用户只是不想在 GitHub 首页文件列表里看到开发过程提交，可以用一次正式发布提交触碰需要展示的路径，让 “Latest commit” 列统一成中性的发布信息。

不要为了美化首页就自动 squash 或 force-push。重写历史必须再次取得明确授权。

## 临时内容

正式发布前清理一次性 TTS job、render job、单次测试 workflow、cache、`node_modules`、`out/` 和 staging 目录。保留真正的运行脚本、可复用 workflow 模板、references 和最终 Demo。

## 发布状态措辞

区分：

- 文件已生成；
- validator 通过；
- 脚本实际运行通过；
- 已上传 GitHub；
- Plugin manifest 已解析；
- Codex 端到端安装已验证。

不要把前一步成功等同于后一步。
