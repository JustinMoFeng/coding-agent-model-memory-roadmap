# Coding Agent Model and Memory Roadmap

这是一个面向个人长期成长的 Research OS 仓库。

它包含：

- 学习路线与周计划。
- 论文卡片。
- 实验记录。
- Memory / Coding Agent 专题调研。
- GitHub Pages 文档站配置。
- 小型代码实验入口。

文档站源文件在 `content/` 下，站点使用 MkDocs Material 构建。

文档站地址：https://JustinMoFeng.github.io/coding-agent-model-memory-roadmap/

## 本地预览

```bash
make install
make serve
```

`make install` 默认使用清华 PyPI 镜像源，可通过环境变量覆盖：

```bash
PIP_INDEX_URL=https://pypi.org/simple make install
```

## 目录原则

- `content/`：知识库与 GitHub Pages 内容，是主要 source of truth。
- `labs/`：小型代码实验，适合放 tokenizer 观察、toy SFT、memory schema prototype。
- 外部项目 repo：成熟项目单独建仓库，在 `content/projects/` 中写项目说明和链接。
- `scripts/`：生成周计划、每日进度页、论文卡片、实验记录的脚本。

## 起步入口

- 网站首页：[content/index.md](content/index.md)
- 第一周计划：[content/weeks/2026-06-25/index.md](content/weeks/2026-06-25/index.md)
- 周计划模板：[content/reference/templates/week-plan-template.md](content/reference/templates/week-plan-template.md)
- 每日进度模板：[content/reference/templates/daily-log-template.md](content/reference/templates/daily-log-template.md)
