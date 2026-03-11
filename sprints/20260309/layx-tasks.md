# 周冲刺任务

- 迭代周期：2026-03-09 ~ 2026-03-14
- 责任人：赖毅
- 周冲刺计划：`{ops-playbook}/sprints/20260309/sprint-plan.md`
- 工单编号：[crm-product#1](https://github.com/it188-networkx/crm-product/issues/1)
- 更新时间：2026-03-11 11:10

## 待澄清问题 (Open Questions)

无待澄清问题。

## 展开策略 (Expansion Strategy)

本冲刺交付目标为完成 MVP 全部产品设计（S0301 → S0306），任务按阶段逐步展开。
每完成一个阶段的制品后，依据其产出动态添加下一阶段的子任务，直到全部功能特性设计完成。

| 阶段 | SOP | 制品 | 前置阶段 | 范围说明 |
| :--- | :--- | :--- | :--- | :--- |
| 1 - 架构骨架 | S0301 功能架构规划 | A0301 产品需求大纲 | 无 | MVP 全量 Theme 清单与优先级 |
| 2 - 主题定义 | S0302 功能主题规划 | A0302 需求主题定义 | 阶段 1 完成 | 全部 Theme 展开（T-01 营销过程闭环、T-02 AI营销管理、T-03 决策驾驶舱、T-04 营销知识库） |
| 3 - 史诗拆分 | S0303 功能史诗规划 | A0303 需求史诗定义 | 对应 Theme 的阶段 2 完成 | 从已完成 Theme 展开 Epic |
| 4 - 特性定义 | S0304 功能特性规划 | A0304 需求特性定义 | 对应 Epic 的阶段 3 完成 | 从 P0 Epic 展开 Feature |
| 5 - 特性设计 | S0306 功能特性设计 | A0306 特性设计文档 | 对应 Feature 的阶段 4 完成 | lowcode 变体，逐 Feature 产出设计方案 |

## 状态总览 (Status Overview)

| 任务编号 | 任务描述 | 关联工单 | 预计完成 | 实际完成 | 工作量 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101201 | S0301 功能架构规划：编制 CRM 产品需求大纲（A0301） | [#2](https://github.com/it188-networkx/crm-product/issues/2) | 03-11 | 03-11 | 0.5 天 | 已完成 |
| 101202 | S0302 功能主题规划：T-01 营销过程闭环（A0302） | [#4](https://github.com/it188-networkx/crm-product/issues/4) | 03-11 | - | 0.5 天 | 已执行 |
| 101203 | S0302 功能主题规划：T-02 AI营销管理（A0302） | 待开设 | 03-11 | - | 0.5 天 | 未开始 |
| 101204 | S0302 功能主题规划：T-03 决策驾驶舱（A0302） | 待开设 | 03-13 | - | 0.5 天 | 未开始 |
| 101205 | S0302 功能主题规划：T-04 营销知识库（A0302） | 待开设 | 03-14 | - | 0.5 天 | 未开始 |

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
- 功能架构规划工单模版：`.github/ISSUE_TEMPLATE/03-01-prd-master.yml`
- 上游制品：`{ops-playbook}/sprints/20260309/sprint-plan.md` 第 1012 行
- 过程参考：`{ops-playbook}/sops/workflow/product-design.md`（W301 产品需求规划章节）

**处理规程**

SOP：`{product-base}/process/sop-prd-master.md`（S0301 功能架构规划）
工单模版：`.github/ISSUE_TEMPLATE/03-01-prd-master.yml`

**预期制品**

- 制品：`requirements/requirements.md`（A0301 产品需求大纲），包含 MVP 功能范围确认、Theme / Epic / Feature 三级层次索引与各 Theme 简要定义
- 模板：`{product-base}/template/requirements/prd-master.md`

---

### 101202 S0302 功能主题规划：T-01 营销过程闭环

**任务概要**

- 目标：按 S0302 功能主题规划 SOP，基于 A0301 产品需求大纲中 T-01「营销过程闭环」定义，产出 A0302 需求主题定义（`requirements/structured-sales-cycle/README.md`），包含业务背景、核心目标、价值承诺、端到端用户旅程、Epic 拆分索引与验收标准，为后续 S0303 功能史诗规划提供输入
- 关联工单：[crm-product#4](https://github.com/it188-networkx/crm-product/issues/4)
- 关联 PR：[crm-product#5](https://github.com/it188-networkx/crm-product/pull/5)
- 预计完成：03-11
- 工作量估算：0.5 天
- 状态：已执行

---

**上下文**

- 产品需求大纲（A0301）：`requirements/requirements.md`，T-01 价值主张：让销售与市场在统一流程中完成从线索录入、评分分级、培育触达到商机推进、成交复盘的端到端闭环
- 产品定义文档（A0203）：`concept/product-definition.md`，§1.4 MVP 包含范围「结构化销售闭环」
- 用户画像（A0103）：`discovery/users/mkt-persona.md`、`discovery/users/sales-persona.md`（已就绪）
- 全局约束：A0301 §3 GC-01 AI建议边界、GC-04 操作审计、GC-05 最小录入、GC-06 权限分级（均影响 T-01）
- 核心指标：月均有效跟进客户数（当前 ≤ 30 家 → 目标 ≥ 100 家 M6）、跟进备案工时（≥ 3h/次 → ≤ 30min/次 M6）

**处理规程**

SOP：`{product-base}/process/sop-prd-theme.md`（S0302 功能主题规划）
工单模版：`.github/ISSUE_TEMPLATE/03-02-prd-theme.yml`

**预期制品**

- 制品：`requirements/structured-sales-cycle/README.md`（A0302 需求主题定义 T-01）
- 模板：`{product-base}/template/requirements/prd-theme.md`

---

### 101203 S0302 功能主题规划：T-02 AI营销管理

**任务概要**

- 目标：按 S0302 功能主题规划 SOP，基于 A0301 产品需求大纲中 T-02「AI营销管理」定义，产出 A0302 需求主题定义（`requirements/ai-augmentation/README.md`），包含业务背景、核心目标、价值承诺、端到端用户旅程、Epic 拆分索引与验收标准，为后续 S0303 功能史诗规划提供输入
- 关联工单：待开设
- 预计完成：03-11
- 工作量估算：0.5 天
- 状态：未开始

---

**上下文**

- 产品需求大纲（A0301）：`requirements/requirements.md`，T-02 价值主张：以 AI 承担线索评分、跟进建议、内容草稿生成与竞品预警等可标准化运营工作，将有限人力的有效覆盖规模放大至 ≥ 3 倍
- 产品定义文档（A0203）：`concept/product-definition.md`，§1.4 MVP 包含范围「AI 增效工作流」
- 用户画像（A0103）：`discovery/users/mkt-persona.md`、`discovery/users/sales-persona.md`、`discovery/users/presales-persona.md`（已就绪）
- 全局约束：A0301 §3 GC-01 AI建议边界（AI 所有输出须经人工确认）、GC-03 信息脱敏（影响 T-02）
- 核心指标：AI 建议满意度（无基线 → ≥ 3.5/5 M3）、核心用户周活跃率（≥ 70% M3）

**处理规程**

SOP：`{product-base}/process/sop-prd-theme.md`（S0302 功能主题规划）
工单模版：`.github/ISSUE_TEMPLATE/03-02-prd-theme.yml`

**预期制品**

- 制品：`requirements/ai-augmentation/README.md`（A0302 需求主题定义 T-02）
- 模板：`{product-base}/template/requirements/prd-theme.md`

---

### 101204 S0302 功能主题规划：T-03 决策驾驶舱

**任务概要**

- 目标：按 S0302 功能主题规划 SOP，基于 A0301 产品需求大纲中 T-03「决策驾驶舱」定义，产出 A0302 需求主题定义（`requirements/executive-dashboard/README.md`），包含业务背景、核心目标、价值承诺、端到端用户旅程、Epic 拆分索引与验收标准，为后续 S0303 功能史诗规划提供输入
- 关联工单：待开设
- 预计完成：03-13
- 工作量估算：0.5 天
- 状态：未开始

---

**上下文**

- 产品需求大纲（A0301）：`requirements/requirements.md`，T-03 价值主张：为管理层提供漏斗全链路、渠道 ROI 对比与商机健康度预警的统一视图，让老板基于可信数据自助判断资源分配与介入时机
- 产品定义文档（A0203）：`concept/product-definition.md`，§1.4 MVP 包含范围「老板决策看板」；§3.1 买单方画像（CEO/王总）
- 用户画像（A0103）：`discovery/users/ceo-persona.md`（已就绪）
- 全局约束：A0301 §3 GC-02 数据主权、GC-04 操作审计、GC-06 权限分级（均影响 T-03）
- 核心指标：老板通过系统做投入决策占比（0% → ≥ 60% M6）

**处理规程**

SOP：`{product-base}/process/sop-prd-theme.md`（S0302 功能主题规划）
工单模版：`.github/ISSUE_TEMPLATE/03-02-prd-theme.yml`

**预期制品**

- 制品：`requirements/executive-dashboard/README.md`（A0302 需求主题定义 T-03）
- 模板：`{product-base}/template/requirements/prd-theme.md`

---

### 101205 S0302 功能主题规划：T-04 营销知识库

**任务概要**

- 目标：按 S0302 功能主题规划 SOP，基于 A0301 产品需求大纲中 T-04「营销知识库」定义，产出 A0302 需求主题定义（`requirements/knowledge-repository/README.md`），包含业务背景、核心目标、价值承诺、端到端用户旅程、Epic 拆分索引与验收标准，为后续 S0303 功能史诗规划提供输入
- 关联工单：待开设
- 预计完成：03-14
- 工作量估算：0.5 天
- 状态：未开始

---

**上下文**

- 产品需求大纲（A0301）：`requirements/requirements.md`，T-04 价值主张：将行业解决方案、成功案例与竞品应对经验结构化归档，形成公司级可复用知识资产，支撑 AI 建议的行业贴合度与售前团队的快速响应能力
- 产品定义文档（A0203）：`concept/product-definition.md`，§1.4 MVP 包含范围「知识沉淀体系」
- 用户画像（A0103）：`discovery/users/presales-persona.md`、`discovery/users/mkt-persona.md`（已就绪）
- 全局约束：A0301 §3 GC-02 数据主权、GC-03 信息脱敏、GC-04 操作审计（均影响 T-04）
- 核心指标：年化人力节省等效（¥0 → ≥ ¥50 万 M12，T-04 贡献售前响应效率提升）

**处理规程**

SOP：`{product-base}/process/sop-prd-theme.md`（S0302 功能主题规划）
工单模版：`.github/ISSUE_TEMPLATE/03-02-prd-theme.yml`

**预期制品**

- 制品：`requirements/knowledge-repository/README.md`（A0302 需求主题定义 T-04）
- 模板：`{product-base}/template/requirements/prd-theme.md`

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
- [x] 后续阶段任务已在 101201 完成后动态添加（101202 / 101203 / 101204 / 101205）
- [ ] 已将 A2002 路径回写至 A2001 "个人冲刺任务"区块
