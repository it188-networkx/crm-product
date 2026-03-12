# 周冲刺任务

- 迭代周期：2026-03-09 ~ 2026-03-14
- 责任人：赖毅
- 周冲刺计划：`{ops-playbook}/sprints/20260309/sprint-plan.md`
- 工单编号：crm-product#1
- 更新时间：2026-03-14（S0304 全量 Epic 补充完成）

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

## 冲刺任务 (Sprint Tasks)

| 任务编号 | 任务描述 | 制品路径 | 关联工单 | 关联 PR | 状态 | 完成日期 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [101201](./t101201.md) | S0301 功能架构规划：编制 CRM 产品需求大纲（A0301） | `requirements/prd-master.md` | #2 | #3 | 已完成 | 03-11 |
| [101202](./t101202.md) | S0302 功能主题规划：T-01 营销过程闭环（A0302） | `requirements/marketing-closed-loop/README.md` | #4 | #5 | 已完成 | 03-11 |
| [101203](./t101203.md) | S0302 功能主题规划：T-02 AI营销管理（A0302） | `requirements/ai-augmentation/README.md` | #6 | #7 | 已完成 | 03-11 |
| [101204](./t101204.md) | S0302 功能主题规划：T-03 决策驾驶舱（A0302） | `requirements/decision-cockpit/README.md` | #8 | #9 | 已完成 | 03-11 |
| [101205](./t101205.md) | S0302 功能主题规划：T-04 营销知识库（A0302） | `requirements/knowledge-base/README.md` | #10 | #11 | 已完成 | 03-11 |
| [101301](./t101301.md) | S0303 功能史诗规划：T-01/E-01 线索治理与分配（A0303） | `requirements/marketing-closed-loop/lead-governance/README.md` | #14 | #15 | 已完成 | 03-13 |
| [101302](./t101302.md) | S0303 功能史诗规划：T-01/E-02 培育与跟进沉淀（A0303） | `requirements/marketing-closed-loop/nurture-followup/README.md` | #16 | #22 | 已完成 | 03-13 |
| [101303](./t101303.md) | S0303 功能史诗规划：T-01/E-03 商机推进与阶段门控（A0303） | `requirements/marketing-closed-loop/opportunity-pipeline/README.md` | #17 | #23 | 已完成 | 03-13 |
| [101304](./t101304.md) | S0303 功能史诗规划：T-01/E-04 成交复盘与策略回流（A0303） | `requirements/marketing-closed-loop/deal-retrospective/README.md` | #18 | #24 | 已完成 | 03-13 |
| [101305](./t101305.md) | S0303 功能史诗规划：T-01/E-05 营销自动化规则管理（A0303） | `requirements/marketing-closed-loop/automation-rules/README.md` | #19 | #25 | 已完成 | 03-13 |
| [101306](./t101306.md) | S0303 功能史诗规划：T-01/E-06 客户标签体系管理（A0303） | `requirements/marketing-closed-loop/customer-tagging/README.md` | #20 | #26 | 已完成 | 03-13 |
| [101307](./t101307.md) | S0303 功能史诗规划：T-01/E-07 数据接入与同步（A0303） | `requirements/marketing-closed-loop/data-ingestion/README.md` | #21 | #27 | 已完成 | 03-13 |
| [101308](./t101308.md) | S0303 功能史诗规划：T-02/E-01 AI 线索智能研判（A0303） | `requirements/ai-augmentation/lead-intelligence/README.md` | #28 | #29 | 已完成 | 03-12 |
| [101309](./t101309.md) | S0303 功能史诗规划：T-02/E-02 AI 跟进辅助（A0303） | `requirements/ai-augmentation/followup-copilot/README.md` | #30 | #34 | 已完成 | 03-12 |
| [101310](./t101310.md) | S0303 功能史诗规划：T-02/E-03 竞品预警与监控（A0303） | `requirements/ai-augmentation/competitive-alerts/README.md` | #32 | #35 | 已完成 | 03-12 |
| [101311](./t101311.md) | S0303 功能史诗规划：T-03/E-01 销售漏斗全链路视图（A0303） | `requirements/decision-cockpit/sales-funnel-view/README.md` | #36 | #37 | 已完成 | 03-13 |
| [101312](./t101312.md) | S0303 功能史诗规划：T-03/E-02 渠道 ROI 对比分析（A0303） | `requirements/decision-cockpit/channel-roi-analysis/README.md` | #38 | #39 | 已完成 | 03-13 |
| [101313](./t101313.md) | S0303 功能史诗规划：T-03/E-03 商机健康度预警（A0303） | `requirements/decision-cockpit/opportunity-health-alert/README.md` | #40 | #41 | 已完成 | 03-13 |
| [101314](./t101314.md) | S0303 功能史诗规划：T-03/E-04 Go/No-Go 验收看板（A0303） | `requirements/decision-cockpit/go-nogo-board/README.md` | #42 | #43 | 已完成 | 03-13 |
| [101315](./t101315.md) | S0303 功能史诗规划：T-04/E-01 知识资产结构化录入与审核（A0303） | `requirements/knowledge-base/knowledge-curation/README.md` | #44 | #45 | 已完成 | 03-13 |
| [101316](./t101316.md) | S0303 功能史诗规划：T-04/E-02 知识检索与场景推送（A0303） | `requirements/knowledge-base/knowledge-retrieval/README.md` | #46 | #47 | 已完成 | 03-13 |
| [101317](./t101317.md) | S0303 功能史诗规划：T-04/E-03 AI 知识向量化引用（A0303） | `requirements/knowledge-base/ai-vectorization/README.md` | #48 | #49 | 已完成 | 03-13 |
| [101401](./t101401.md) | S0304 功能特性规划：T-01/E-01 线索治理与分配（A0304） | `requirements/structured-sales-cycle/lead-governance/<feature>/README.md` ×4 | #50 | #52 | 已派发 | - |
| [101402](./t101402.md) | S0304 功能特性规划：T-01/E-02 培育与跟进沉淀（A0304） | `requirements/structured-sales-cycle/nurture-followup/<feature>/README.md` ×3 | #54 | #58 | 已派发 | - |
| [101403](./t101403.md) | S0304 功能特性规划：T-01/E-03 商机推进与阶段门控（A0304） | `requirements/structured-sales-cycle/opportunity-pipeline/<feature>/README.md` ×3 | #55 | #60 | 已派发 | - |
| [101404](./t101404.md) | S0304 功能特性规划：T-01/E-04 成交复盘与策略回流（A0304） | `requirements/structured-sales-cycle/winloss-retrospective/<feature>/README.md` ×3 | #51 | #53 | 已派发 | - |
| [101405](./t101405.md) | S0304 功能特性规划：T-01/E-05 营销自动化规则管理（A0304） | `requirements/structured-sales-cycle/marketing-automation/<feature>/README.md` ×2 | #56 | #62 | 已派发 | - |
| [101406](./t101406.md) | S0304 功能特性规划：T-01/E-06 客户标签体系管理（A0304） | `requirements/structured-sales-cycle/tag-management/<feature>/README.md` ×3 | #57 | #64 | 已派发 | - |
| [101407](./t101407.md) | S0304 功能特性规划：T-01/E-07 数据接入与同步（A0304） | `requirements/structured-sales-cycle/data-integration/<feature>/README.md` ×3 | #59 | #68 | 已派发 | - |
| [101408](./t101408.md) | S0304 功能特性规划：T-02/E-01 AI 线索智能研判（A0304） | `requirements/ai-augmentation/lead-intelligence/<feature>/README.md` ×3 | #61 | #67 | 已派发 | - |
| [101409](./t101409.md) | S0304 功能特性规划：T-02/E-02 AI 跟进辅助（A0304） | `requirements/ai-augmentation/followup-copilot/<feature>/README.md` ×3 | #63 | #69 | 已派发 | - |
| [101410](./t101410.md) | S0304 功能特性规划：T-03/E-01 销售漏斗全链路视图（A0304） | `requirements/executive-dashboard/funnel-analytics/<feature>/README.md` ×3 | #65 | #70 | 已派发 | - |
| [101411](./t101411.md) | S0304 功能特性规划：T-03/E-02 渠道 ROI 对比分析（A0304） | `requirements/executive-dashboard/channel-roi/<feature>/README.md` ×3 | #66 | #71 | 已派发 | - |
| [101412](./t101412.md) | S0304 功能特性规划：T-02/E-03 竞品预警与监控（A0304） | `requirements/ai-augmentation/competitive-alerts/competitive-alert-push/README.md` ×1 | #72 | - | 已派发 | - |
| [101413](./t101413.md) | S0304 功能特性规划：T-03/E-03 商机健康度预警（A0304） | `requirements/executive-dashboard/opportunity-health/<feature>/README.md` ×5 | #73 | - | 已派发 | - |
| [101414](./t101414.md) | S0304 功能特性规划：T-03/E-04 Go/No-Go 验收看板（A0304） | `requirements/executive-dashboard/go-nogo-dashboard/<feature>/README.md` ×4 | #74 | - | 已派发 | - |
| [101415](./t101415.md) | S0304 功能特性规划：T-04/E-01 知识资产结构化录入与审核（A0304） | `requirements/knowledge-repository/knowledge-ingestion/<feature>/README.md` ×3 | #75 | - | 已派发 | - |
| [101416](./t101416.md) | S0304 功能特性规划：T-04/E-02 知识检索与场景推送（A0304） | `requirements/knowledge-repository/knowledge-retrieval/<feature>/README.md` ×3 | #77 | - | 已派发 | - |
| [101417](./t101417.md) | S0304 功能特性规划：T-04/E-03 AI 知识向量化引用（A0304） | `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md` ×1 | #80 | - | 已派发 | - |

> S0302 主题定义阶段全部 4 个 Theme（T-01 ~ T-04）均已完成（截至 03-11）。
> S0303 史诗拆分阶段全部 17 个 Epic（101301 ~ 101317）均已完成（截至 03-13）。
> S0304 功能特性规划全部 17 个 Epic 任务已规划（101401 ~ 101417）：T-01 E-01~E-07（7 个）、T-02 E-01~E-03（3 个）、T-03 E-01~E-04（4 个）、T-04 E-01~E-03（3 个）。T-04 知识库交付阶段为 Phase 2，但产品设计（需求特性定义）在本冲刺范围内完成。

## 自检清单 (Self-Check)

- [x] A2002 文件存在于 `crm-product/sprints/20260309/layx-tasks/README.md`
- [x] 任务清单覆盖 A2001 中分配给本人的全部交付目标（1012）
- [x] 初始任务（101201）包含四要素（任务目标/上下文/处理规程/预期制品）
- [x] 任务对齐 W301 产品设计流程中的具体 SOP（S0301）
- [x] 待澄清问题已全部解决并清空（Q001/Q002 结论已融入任务上下文与逐步展开路径）
- [x] 已将 A2002 路径回写至 A2001 "个人冲刺任务"区块
- [ ] 有疑问或无法承接的任务已在备注标注 `[待确认]` 并告知敏捷教练
- [x] 展开策略已明确：S0301 → S0302 → S0303 → S0304 → S0306（lowcode），全部在本冲刺内完成
- [x] 任务按阶段动态展开，每完成一阶段制品后添加下一阶段子任务
- [x] 模板路径已修正：A0301 → `prd-master.md`
- [x] 后续阶段任务已在 101201 完成后动态添加（101202 / 101203 / 101204 / 101205）
- [x] 第三批 S0303 史诗拆分任务已补充规划（101301 ~ 101317，全部 4 个 Theme 共 17 个 Epic）
- [x] 第四批 S0304 功能特性规划任务已补充规划（101401 ~ 101404，T-01 核心管线 E-01/E-02/E-03/E-04）
- [x] 第五批 S0304 功能特性规划任务已补充规划（101405 ~ 101411，T-01 E-05~E-07、T-02 E-01~E-02、T-03 E-01~E-02）
- [x] 第六批 S0304 补充规划任务已添加（101412 ~ 101417，T-02 E-03、T-03 E-03~E-04、T-04 E-01~E-03），覆盖全部 17 个 Epic
