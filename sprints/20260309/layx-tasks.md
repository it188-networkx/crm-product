# 周冲刺任务

- 迭代周期：2026-03-09 ~ 2026-03-14
- 责任人：赖毅
- 周冲刺计划：`{ops-playbook}/sprints/20260309/sprint-plan.md`
- 工单编号：[crm-product#1](https://github.com/it188-networkx/crm-product/issues/1)
- 更新时间：2026-03-11 10:00

## 待澄清问题 (Open Questions)

无待澄清问题。

## 展开策略 (Expansion Strategy)

本冲刺交付目标为完成 MVP 全部产品设计（S0301 → S0306），任务按阶段逐步展开。
每完成一个阶段的制品后，依据其产出动态添加下一阶段的子任务，直到全部功能特性设计完成。

| 阶段 | SOP | 制品 | 前置阶段 | 范围说明 |
| :--- | :--- | :--- | :--- | :--- |
| 1 - 架构骨架 | S0301 功能架构规划 | A0301 产品需求大纲 | 无 | MVP 全量 Theme 清单与优先级 |
| 2 - 主题定义 | S0302 功能主题规划 | A0302 需求主题定义 | 阶段 1 完成 | 逐个 P0 Theme 展开（销售过程闭环、AI营销管理、决策驾驶舱） |
| 3 - 史诗拆分 | S0303 功能史诗规划 | A0303 需求史诗定义 | 对应 Theme 的阶段 2 完成 | 从已完成 Theme 展开 Epic |
| 4 - 特性定义 | S0304 功能特性规划 | A0304 需求特性定义 | 对应 Epic 的阶段 3 完成 | 从 P0 Epic 展开 Feature |
| 5 - 特性设计 | S0306 功能特性设计 | A0306 特性设计文档 | 对应 Feature 的阶段 4 完成 | lowcode 变体，逐 Feature 产出设计方案 |

## 状态总览 (Status Overview)

| 任务编号 | 任务描述 | 关联工单 | 预计完成 | 实际完成 | 工作量 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101201 | S0301 功能架构规划：编制 CRM 产品需求大纲（A0301） | [#2](https://github.com/it188-networkx/crm-product/issues/2) | 03-12 | 03-11 | 0.5 天 | 已完成 |

## 冲刺任务 (Sprint Tasks)

### 101201 S0301 功能架构规划：编制 CRM 产品需求大纲

**任务概要**

- 目标：按 S0301 功能架构规划 SOP，基于 A0203 产品定义文档 §1.4 MVP 范围直接推导 CRM 产品需求大纲（A0301），锁定 MVP Theme 清单与优先级排序，为后续 S0302 功能主题规划提供顶层框架输入。Theme 划分需与路线图 Q1 战略主题（销售过程闭环、AI营销管理）对齐
- 关联工单：[crm-product#2](https://github.com/it188-networkx/crm-product/issues/2)
- 关联 PR：[crm-product#3](https://github.com/it188-networkx/crm-product/pull/3)
- 预计完成：03-11
- 实际完成：03-11
- 工作量估算：0.5 天
- 状态：已完成

---

**上下文**

- 产品定义文档（A0203）：`concept/product-definition.md`（草稿状态），Section 1.4 MVP 包含范围定义了 4 大功能域（AI 增效工作流、结构化销售闭环、知识沉淀体系、老板决策看板）；Section 1.5 里程碑定义了 M1-M12 交付节奏
- 商业需求文档（A0202）：`concept/business-requirement.md`（草稿状态），Section 2 内部效率目标提供 M1/M3/M6/M12 验收指标
- 产品概念书（A0201）：`concept/product-concept.md`（草稿状态），Section 6 初步范围
- 需求分析报告（A0106）：`discovery/requirements/` — 目录不存在，本迭代基于 A0203 直接推导
- 需求变更记录（A0305）：无（新产品无历史变更）
- 需求目录规范：`requirements/AGENTS.md`（design-variant = lowcode）
- 功能架构规划 SOP（S0301）：`{product-base}/process/sop-prd-master.md`
- 功能架构规划工单模版：`.github/ISSUE_TEMPLATE/P03-01-prd-master.yml`
- 上游制品：`{ops-playbook}/sprints/20260309/sprint-plan.md` 第 1012 行
- 过程参考：`{ops-playbook}/sops/workflow/product-design.md`（W301 产品需求规划章节）

**处理规程**

SOP：`{product-base}/process/sop-prd-master.md`（S0301 功能架构规划）
工单模版：`.github/ISSUE_TEMPLATE/P03-01-prd-master.yml`

**预期制品**

- 制品：`requirements/requirements.md`（A0301 产品需求大纲），包含 MVP 功能范围确认、Theme / Epic / Feature 三级层次索引与各 Theme 简要定义
- 模板：`{product-base}/template/requirements/prd-master.md`

## 自检清单 (Self-Check)

- [x] A2002 文件存在于 `crm-product/sprints/20260309/layx-tasks.md`
- [x] 任务清单覆盖 A2001 中分配给本人的全部交付目标（1012）
- [x] 初始任务（101201）包含四要素（任务目标/上下文/处理规程/预期制品）
- [x] 任务对齐 W301 产品设计流程中的具体 SOP（S0301）
- [x] 任务粒度符合标准（0.5 天至 2 天）
- [x] 待澄清问题已全部解决并清空（Q001/Q002 结论已融入任务上下文与逐步展开路径）
- [ ] 已将 A2002 路径回写至 A2001 "个人冲刺任务"区块
- [ ] 有疑问或无法承接的任务已在备注标注 `[待确认]` 并告知敏捷教练
- [x] 展开策略已明确：S0301 → S0302 → S0303 → S0304 → S0306（lowcode），全部在本冲刺内完成
- [x] 任务按阶段动态展开，每完成一阶段制品后添加下一阶段子任务
- [x] 模板路径已修正：A0301 → `prd-master.md`
- [x] 后续阶段任务待 101201 完成后根据产出动态添加
