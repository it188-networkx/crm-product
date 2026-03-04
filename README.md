# CRM 产品管理仓库

本仓库提供覆盖 CRM (Customer Relationship Management) 产品全生命周期的设计文档，可以为 AI First 的产品编码、测试和部署提供完整的上下文信息。

> 本仓库遵循 [product-template](https://github.com/it188-networkx/product-template) 标准目录结构。

## 主要内容

以下是仓库的主要内容，按产品生命周期阶段排列。

| 阶段 | 目录 | 阶段名称 | 说明 |
|----------|------|----------|------|
| P01 | [discovery/](discovery/) | 需求发现 | 市场调研、用户研究、竞品分析、需求收集 |
| P02 | [concept/](concept/) | 产品概念 | 产品定义、商业论证（商业需求文档）、MVP 范围界定 |
| P03 | [requirements/](requirements/) | 需求规划 | Master PRD、Epic 规划、Feature 拆解、决策记录 |
| P04 | [roadmap/](roadmap/) | 产品路线图 | 里程碑计划、版本规划、优先级排序 |
| P05 | [architecture/](architecture/) | 架构设计 | 系统架构、模块划分、集成方案 |
| P06 | [technology/](technology/) | 技术选型 | 技术栈选择、评估报告、选型决策 |
| P07 | [ui/](ui/) | UI 设计 | 视觉设计、设计规范、组件说明 |
| P08 | design | 产品设计 | 交互设计、功能规格、设计评审，位于代码仓库 |
| P09 | coding | 产品编码 | 编码规范、实现方案、代码结构，位于代码仓库 |
| P10 | testing | 产品测试 | 测试计划、测试用例、测试报告，位于测试仓库 |
| P11 | deploy | 部署交付 | 部署方案、环境配置、发布流程，位于部署仓库 |
| P12 | [enablement/](enablement/) | 销售赋能材料 | 培训资料、演示文稿、常见问题解答 |
| P13 | [evolution/](evolution/) | 产品演进 | 数据分析、PMF 验证、技术风险评估、架构演进路径 |

## 🗂️ 目录结构

```
crm-product/
├── discovery/      # 需求发现（市场调研/用户研究/竞品分析）
├── concept/        # 产品概念书（产品定义/商业需求文档）
├── requirements/   # 需求规格（Theme / Epic / Feature 三级结构）
├── roadmap/        # 产品路线图（里程碑/版本规划）
├── architecture/   # 架构设计（系统架构/ADR 决策记录）
├── technology/     # 技术选型（技术调研/候选方案/选型结论）
├── ui/             # UI 设计（前端架构/视觉规范/组件清单）
├── enablement/     # 销售赋能（案例/销售材料/培训/演示）
├── evolution/      # 产品演进（数据分析/PMF验证/架构演进）
├── references/     # 外部参考资料（行业研报/市场数据/竞品资料）
├── sprints/        # 冲刺任务清单
├── scripts/        # 辅助脚本
└── .github/        # GitHub 配置与 Issue 模板
```

## 🚀 快速导航

- [需求大纲](requirements/requirements.md)
- [产品定义](concept/product-definition.md)
- [产品路线图](roadmap/README.md)
- [架构设计](architecture/architecture.md)
- [Issue 模板](.github/ISSUE_TEMPLATE/)

## 强制规则

**每当新增/删除/重命名目录或重要文件后，必须同步更新根目录 `README.md` 中的以下两处：**

1. `## 🗂️ 目录结构` — 目录树（增删对应行）
2. `## 🚀 快速导航` — 相关导航链接（增删入口）

更新完毕后一并提交，commit message 格式：`docs: update README for <变更内容>`

## Issue 工作流

1. 使用 `.github/ISSUE_TEMPLATE/` 下的模板创建 Issue
2. **接入工单**：在 ops-playbook 中创建（需求入口）
3. Labels 使用 `domain:product` + `activity:requirement` 等组合

## PRD 层级

按 **主题 / Epic / Feature** 三级层次组织（存放于 `requirements/`）：

- **Theme**：客户或业务场景（如"客户管理"、"销售管理"）
- **Epic**：功能模块（如"线索管理"、"商机跟进"）
- **Feature**：具体功能特性（如"线索分配规则"、"赢单分析"）
