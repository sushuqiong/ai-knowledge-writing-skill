<p align="center">
  <img src="assets/repo-cover.svg" alt="AI Knowledge Writing workflow" width="100%" />
</p>

# AI Knowledge Writing Skill

[![Release](https://img.shields.io/github/v/release/sushuqiong/ai-knowledge-writing-skill?display_name=tag)](https://github.com/sushuqiong/ai-knowledge-writing-skill/releases)
[![Validate](https://github.com/sushuqiong/ai-knowledge-writing-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/sushuqiong/ai-knowledge-writing-skill/actions/workflows/validate.yml)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1769E0)](https://agentskills.io/)
[![Privacy](https://img.shields.io/badge/privacy-scanned-0F766E)](SECURITY.md)
[![License](https://img.shields.io/badge/license-MIT-D97706)](LICENSE)

**把“读懂材料、核实事实、原创写作、Word交付、隐私复核”沉淀为一套可复用、可验证的平台中立 Agent Skill。**

[English README](README.en.md) · [在线写作工作台](https://sushuqiong.github.io/ai-knowledge-writing-skill/) · [v0.3.0](https://github.com/sushuqiong/ai-knowledge-writing-skill/releases/tag/v0.3.0)

## 30秒开始

不安装，只查看可发现的 Skill：

```powershell
npx skills add sushuqiong/ai-knowledge-writing-skill --list
```

全局安装：

```powershell
npx skills add sushuqiong/ai-knowledge-writing-skill --skill ai-knowledge-writing-skill -g -y
```

然后向支持 Agent Skills 的客户端提出：

```text
Use $ai-knowledge-writing-skill to turn [topic or source] into an original Chinese public explainer for [audience], verify changing claims, and deliver a privacy-safe DOCX within [length].
```

## 它解决什么问题

很多文案任务并不只是“让AI写一篇文章”。真正困难的是：附件是否可靠、哪些内容需要联网核实、怎样避免贴着原文改写、医学结论如何保留边界、Word文件是否真的能打开，以及公开前有没有泄露隐私。

这个Skill把过程固定为七步：

`明确任务 -> 阅读材料 -> 核实事实 -> 设计结构 -> 原创写作 -> Word交付 -> 隐私与发布复核`

| 常见任务 | 使用的 recipe | 关键检查 |
| --- | --- | --- |
| 概念、方法、流程科普 | `concept-explainer` | 定义、价值、基本操作、结果、误区 |
| 图片、截图、文档解读 | `source-to-article` | 可见事实、推断、缺失信息、原创结构 |
| 医学与高风险主题 | `high-risk-health` | 权威来源、适用人群、证据限制、非诊疗边界 |
| 产品、工具和价格比较 | `product-comparison` | 日期快照、同维度比较、官方来源、成本类型 |
| 词汇和固定清单 | `glossary-list` | 数量、顺序、重复项、一词一句 |
| Word文档交付 | `docx-delivery` | 字数、结构、超链接、元数据、重新打开 |

## 五功能知识工作台仍然保留

公众号写作不是第六个lane，而是组合使用现有能力：

| Lane | 作用 |
| --- | --- |
| `browser-lane` | 阅读来源、截图、论文和当前事实 |
| `visualize-lane` | 生成图表、流程和视觉说明 |
| `sites-lane` | 整理README、Pages和公开页面 |
| `queue-lane` | 安排多篇内容、依赖和插入任务 |
| `precision-lane` | 处理歧义、隐私、原创和证据边界 |

## Word工具

可选的本地工具只处理文件，不联网、不上传、不调用模型：

```powershell
python -m pip install -r requirements.txt
python scripts/render_docx.py --input templates/article.example.json --output dist/example.docx
python scripts/validate_article.py --input templates/article.example.json --docx dist/example.docx
```

正文长度按“小标题 + 正文段落”的非空白字符统计，不计标题、副标题、免责声明和来源。生成器默认不插图，并清空作者、修改者和评论元数据。

## 验证与边界

```powershell
python scripts/validate_public_package.py
python -m unittest discover -s tests -v
```

仓库包含24个行为案例和14项确定性测试。它验证路由、文件结构、字数、超链接、DOCX完整性、元数据和隐私模式，但不会自动证明医学事实正确，也不会替代专业审稿。

所有公开示例均为合成内容或占位符。仓库不包含历史文章、用户附件、私人知识库、本机路径、个人联系方式、凭证、内部链接、遥测或后台服务。详见[原创边界](docs/originality.md)和[安全策略](SECURITY.md)。

## 许可证

本仓库全部内容继续采用 [MIT License](LICENSE)。

