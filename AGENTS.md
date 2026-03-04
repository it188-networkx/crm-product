# CRM 产品管理仓库 - Copilot 上下文

## 仓库结构

> 本仓库遵循 [product-template](https://github.com/it188-networkx/product-template) 标准目录结构。

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

## 强制规则

- 每次变更仓库目录结构后必须同步更新 README.md 的目录树和快速导航两处。
- Issue 必须使用 `.github/ISSUE_TEMPLATE/` 下对应阶段的模板创建。
- 冲刺任务清单存放于 `sprints/<YYYYMMDD>/<user>-tasks.md`，冲刺目录以周一日期命名。

## Issue 工作流

- 使用 `.github/ISSUE_TEMPLATE/` 下的模板创建 Issue。
- 接入工单在 ops-playbook 中创建（需求入口）。
- Labels 使用 `domain:product` + `activity:requirement` 等组合。
