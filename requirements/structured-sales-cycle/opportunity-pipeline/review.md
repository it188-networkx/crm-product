---
description: "Epic Review（史诗审核记录）——商机推进与阶段门控，记录对 E-03 全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-03] 商机推进与阶段门控 (Opportunity Pipeline)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-03] 商机推进与阶段门控 (Opportunity Pipeline)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-03] 商机推进与阶段门控（所属 Theme: [T-01] 结构化销售循环）

**Epic 文档路径：** `requirements/structured-sales-cycle/opportunity-pipeline/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/opportunity-pipeline/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/opportunity-pipeline/opportunity-lifecycle/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/opportunity-pipeline/stage-gating/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/opportunity-pipeline/health-view/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 4 |
| 建议 | 3 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 一般 | `opportunity-pipeline/README.md:功能特性表` | Epic 功能特性表中 F-04 商机详情与时间线标注为"待创建"且无文档链接；Epic 业务场景二 Step 5（介入记录关联至商机时间线）与场景四 Steps 1–3（售前协同、技术评估录入）所依赖的 F-04 能力在当前三个 A0304 文档中均无覆盖，导致本次审核范围存在已知空白 | 尽快执行 S0304 创建 F-04 文档，并在 F-04 建立后重新补充本轮审核中未覆盖的场景步骤发现；在 Epic 文档 F-04 行明确目标交付周期与阻塞说明 |
| F-02 | R2 | 一般 | `opportunity-lifecycle/README.md:业务规则` | F-01 BR-01（门控不可绕过）与 BR-02（阶段规则可配置）分别与 Epic BR-01 和 BR-02 在名称与核心约束内容上完全重叠，但均未使用 `承接 Epic [BR-01]` / `承接 Epic [BR-02]` 标记。Epic BR-01 与 BR-02 是同时适用 F-01 和 F-02 的共享 BR；F-01 以独立条目重述而非引用，违反 SSOT 原则，若 Epic BR 后续修订则 F-01 不会自动同步 | 将 F-01 BR-01 改为仅保留 F-01 增量内容（"本 Feature 仅消费门控结果（通过/阻止）"），并在条目末尾加注 `承接 Epic [BR-01]`；将 F-01 BR-02 同理改为仅保留"须通过 F-02 的配置方式管理"的增量内容并加注 `承接 Epic [BR-02]`；F-01 BR-04 补充 `承接 Epic [BR-04]` 标记（当前仅注明 `承接 E-02`，缺少 Epic BR 引用） |
| F-03 | R3 | 一般 | `opportunity-pipeline/README.md:业务场景四 Step 4` / `stage-gating/README.md:业务规则 BR-02` | Epic 场景四 Step 4 要求"技术评估状态 = 已评估"作为方案沟通→商务谈判的门控条件之一，但 F-02 BR-02 中仅列出三类条件类型（必填字段、最低停留时长、决策人接触状态），未包含"技术评估状态"，也无对应 US/AC 覆盖该门控条件的配置与校验 | 在 F-02 BR-02 中新增"指定状态字段达到目标值"条件类型或明确纳入"技术评估状态"，并在 F-02 用户故事与验收标准中补充对应条目覆盖管理员配置与销售推进校验两个场景 |
| F-04 | R7 | 一般 | `opportunity-pipeline/README.md:非功能需求 NFR-03` / `opportunity-lifecycle/README.md:业务规则 BR-05 与验收标准` | Epic NFR-03 要求漏斗数据更新时延不超过1分钟，但 F-01 BR-05 仅描述"实时输出"，未量化该 SLA；F-01 验收标准中无 AC 覆盖漏斗数据时效性，NFR-03 在 Feature 层缺乏可测试验收口径 | 在 F-01 BR-05 末尾补充"商机状态变更后漏斗数据更新时延不超过1分钟（承接 Epic [NFR-03]）"；在 F-01 验收标准中新增 AC 验证漏斗数据在状态变更后1分钟内同步 |
| F-05 | R5 | 建议 | `opportunity-lifecycle/README.md:业务对象定义-商机记录` / `health-view/README.md:业务规则 BR-03` | F-01 业务对象"商机记录"中定义该属性名为"阶段进入时间"，而 F-03 BR-03 引用该属性时使用"阶段进入时间戳"，两处命名不一致，可能导致下游功能特性设计（A0306）或低代码配置中对同一字段产生歧义 | 统一为"阶段进入时间"（与 F-01 业务对象定义保持一致），将 F-03 BR-03 中的"阶段进入时间戳"修改为"阶段进入时间（由 F-01 维护）" |
| F-06 | R6 | 建议 | `health-view/README.md:业务规则 BR-05` / `health-view/README.md:验收标准` | F-03 BR-05 规定当在途商机超过500条时"须明确提示数据量超限"，但 F-03 验收标准中无对应 AC 覆盖该边界条件（当前 AC-01 仅覆盖500条以内的 Happy Path 加载场景），导致边界行为缺乏可测试验收依据 | 在 F-03 验收标准中补充 AC：前置条件为在途商机数量超过500条，触发动作为销售 Leader 打开健康度视图，预期结果为系统展示数据量超限提示并说明当前在途商机数量（参见 BR-05） |
| F-07 | R7 | 建议 | `stage-gating/README.md:用户故事 US-05` | F-02 US-05 引入"审批人"角色，但该角色在 Epic A0303 的业务场景、功能特性表及角色说明中均未定义；其他 Feature（F-01、F-03）中也未出现该角色，存在跨文档角色定义缺失的问题 | 在 Epic A0303 的约束与依赖章节或功能特性说明中明确"审批人"角色来源（如"规则发布审批由具有审批权限的管理员承担，承接 GC-07"），或在 F-02 特性概述中说明审批人与管理员角色的关系 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 执行 S0304 创建 `opportunity-pipeline/<feature>/README.md`（F-04 商机详情与时间线），并在 Epic 功能特性表 F-04 行补充文档链接与目标交付周期说明 | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02 | 修改 `opportunity-lifecycle/README.md:业务规则` 中 BR-01 与 BR-02：仅保留 F-01 增量约束内容，并分别加注 `承接 Epic [BR-01]` 与 `承接 Epic [BR-02]`；同时在 BR-04 末尾补充 `承接 Epic [BR-04]` 标记 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-03 | 修改 `stage-gating/README.md:业务规则 BR-02`，将"技术评估状态"纳入准入条件支持类型；并在用户故事与验收标准中补充对应 US 与 AC，覆盖管理员配置及销售推进时系统校验该条件的流程 | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 修改 `opportunity-lifecycle/README.md:业务规则 BR-05`，补充"商机状态变更后漏斗数据更新时延不超过1分钟（承接 Epic [NFR-03]）"约束；并在验收标准中新增 AC 覆盖漏斗数据时效性的验收口径 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 将 `health-view/README.md:业务规则 BR-03` 中"阶段进入时间戳"统一修改为"阶段进入时间（由 F-01 维护）"，与 F-01 业务对象定义保持命名一致 | 产品负责人 | P2 | 待处理 |
| ACT-06 | F-06 | 在 `health-view/README.md:验收标准` 中新增边界 AC，覆盖在途商机超过500条时系统须展示数据量超限提示的验收场景（参见 BR-05） | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-07 | 在 `opportunity-pipeline/README.md`（Epic 文档）约束与依赖章节或在 `stage-gating/README.md` 特性概述中补充"审批人"角色的来源说明（承接 GC-07，角色取自具有审批权限的管理员群体） | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01、F-02、F-03；F-04 文档不存在，已在 R1 中记录为发现）
- [x] R1 Feature 覆盖完备性检查已执行
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验）
- [x] R3 用户故事完备性检查已执行（步骤覆盖、US-AC 双向追溯）
- [x] R4 BR 引用一致性检查已执行（引用正确性、矛盾检查、四要素检查）
- [x] R5 业务对象协调性检查已执行（命名、属性、状态、语义层）
- [x] R6 验收标准协调性检查已执行（冗余、矛盾、覆盖度、引用闭合）
- [x] R7 跨 Feature 一致性检查已执行（角色、编号、依赖、范围、NFR）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致
- [x] 改进事项已为每条严重/一般级别的发现创建 Action
