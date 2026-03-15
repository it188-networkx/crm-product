---
description: "Epic Review（史诗审核记录）——[E-01] 线索治理与分配，记录对该 Epic 下全部 Feature 定义的系统性审核结论与改进事项"
title: "Epic Review - [E-01] 线索治理与分配 (Lead Governance & Assignment)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-01] 线索治理与分配 (Lead Governance & Assignment)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-01] 线索治理与分配（所属 Theme: structured-sales-cycle）

**Epic 文档路径：** `requirements/structured-sales-cycle/lead-governance/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/lead-governance/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/lead-governance/lead-intake/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/lead-governance/lead-scoring/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/lead-governance/lead-assignment/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/lead-governance/scoring-rule-mgmt/README.md` |

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
| F-01 | R1 | 一般 | `lead-governance/README.md:功能特性` | F-04（线索池管理，P1）在 Epic 功能特性表中标注"待创建"，无对应 A0304 文档。Epic 场景三步骤 1 明确依赖 F-04 线索池视图作为再分配操作的入口，Epic 正文虽提及降级路径（通过线索详情页直接触发再分配），但该降级路径未在任何已定义 Feature 的业务规则或 AC 中正式承接，导致该业务能力缺少下游 S0306 设计的输入基线。 | 针对 F-04 执行 [S0304] 功能特性规划，建立 `lead-pool-mgmt/README.md`，完成用户故事、业务规则与验收标准；同时在 F-03 `lead-assignment/README.md:业务规则` 中补充一条 BR，声明对 F-04 的依赖关系及 F-04 未就绪时的降级入口（线索详情页触发）。 |
| F-02 | R2 | 一般 | `lead-assignment/README.md:业务规则` | Epic [DEP-03] 权限体系依赖（线索分配边界及各角色可见范围依赖 GC-06）在 F-03 的业务规则章节中未通过 `参见 Epic [DEP-03]` 格式正式承接。F-03 BR-03 仅以 TBD 注记方式提及 GC-06 的账号状态校验，完全未覆盖 DEP-03 中"各角色可见范围"维度的约束承接，与 SOP R2 映射（4）要求不符。 | 在 `lead-assignment/README.md:业务规则` 中新增或修改一条 BR，通过 `参见 Epic [DEP-03]` 正式承接权限体系约束，并明确线索分配边界（哪些角色可见、可操作哪些线索）在 GC-06 未就绪时的降级策略（当前默认全员可见，信息隔离风险须在文档中显式标记）。 |
| F-03 | R3 | 一般 | `lead-assignment/README.md:用户故事` | F-03 缺少对 Epic 场景三步骤 2 的覆盖。场景三第 2 步要求"系统提示当前分配状态与跟进记录，供管理者参考分配决策"，但 F-03 用户故事（US-01 至 US-04）和验收标准（AC-01 至 AC-06）中均无对应内容覆盖该决策支撑展示能力；US-03/AC-04 仅覆盖再分配执行操作，未覆盖执行前的信息展示步骤。 | 在 `lead-assignment/README.md:用户故事` 中补充一条 US：作为 MKT Leader / 销售 Leader，在发起再分配前查看目标线索的当前分配状态与跟进记录，从而做出有据可依的再分配决策；同步在验收标准中补充对应 AC，覆盖展示"当前负责销售标识 + 最近跟进记录"的 Happy Path 及"无跟进记录"的边界场景。 |
| F-04 | R6 | 一般 | `lead-scoring/README.md:验收标准` | F-02 BR-02 明确定义了 E-06 标签体系不可用时的降级路径（"降级为仅使用手工标注的行业与规模字段，AI 评分准确度受限须在系统中明确说明"，参见 Epic [DEP-02]），但验收标准（AC-01 至 AC-05）中无对应 AC 覆盖此降级路径，异常路径缺失导致该场景无法通过 AC 验收。 | 在 `lead-scoring/README.md:验收标准` 中补充一条 AC：前置条件为 E-06 标签体系不可用，触发动作为线索入池触发评分，预期结果为系统仅使用手工标注的行业与规模字段完成评分计算并在界面明确提示"评分维度不完整，准确度受限"；关联 US-01 和 BR-02。 |
| F-05 | R3 | 建议 | `lead-intake/README.md:用户故事` | Epic 场景一步骤 1 描述"系统接收 E-07 汇入的新线索数据并执行去重校验"，属于系统自动触发的接入动作，不需要用户主动操作。F-01 的全部用户故事（US-01 至 US-03）均以用户主动提交为前提（角色为 MKT Leader / 运维人员），缺少覆盖"E-07 自动批量汇入后系统自动执行去重校验"的 US/AC，该路径的行为边界（批量汇入命中重复记录时如何处理）依赖 BR 推断而无 AC 可验收。 | 在 `lead-intake/README.md:用户故事` 中补充一条 US，或在现有 US-01 中明确区分"手工提交"与"E-07 自动汇入"两个触发路径，并在验收标准中补充针对批量自动汇入时命中重复记录的 AC（批量场景下合并确认的处置方式）。 |
| F-06 | R3 | 建议 | `lead-governance/README.md:业务场景` | Epic 场景一步骤 5 表述"系统按分级结果自动触发高意向线索的分配路由，将其流转至指定销售"，其中"将其流转至指定销售"暗示自动执行归属关系变更，与 Epic BR-04"分配推荐排序同样仅作参考，不得自动分配"及 F-03 BR-02"须由 MKT Leader 或销售 Leader 人工确认执行"存在语义歧义。F-03 的实现已正确遵循 BR-04，但场景描述本身可能对后续设计或测试人员造成误导。 | 修改 `lead-governance/README.md:业务场景` 中场景一步骤 5 的表述，将"将其流转至指定销售"修改为"生成分配推荐供管理者确认"，以明确该步骤仅产生分配推荐而非执行自动归属变更，与 BR-04 保持语义一致。 |
| F-07 | R5 | 建议 | `lead-assignment/README.md:业务规则` | F-03 BR-02 引用了"分配池"概念（"A 或 B 级的线索进入分配池"），但"分配池"在 F-03 业务对象定义章节中未作定义，在 F-04（待创建）或其他已定义 Feature 的业务对象中亦无定义，形成悬空业务概念引用，下游设计时无法确定该概念的业务职责与属性边界。 | 在 `lead-assignment/README.md:业务对象定义` 中补充"分配池"的简短业务说明（定义其为"已确认分级为 A 或 B 级、待分配的线索集合"），或在 BR-02 中将"分配池"替换为更直接的表述（"进入待分配队列"），避免引入未定义的业务术语。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 执行 [S0304] 为 F-04 创建 `lead-pool-mgmt/README.md`，补全用户故事、业务规则与验收标准；同时在 `lead-assignment/README.md:业务规则` 中补充 F-04 依赖声明及降级入口说明 | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02 | 在 `lead-assignment/README.md:业务规则` 中新增 BR，通过 `参见 Epic [DEP-03]` 正式承接权限体系约束，覆盖角色可见范围约束与 GC-06 未就绪时的降级声明 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-03 | 在 `lead-assignment/README.md:用户故事` 中补充再分配决策支撑 US，并在验收标准中补充对应 AC（展示当前分配状态与跟进记录）| 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 在 `lead-scoring/README.md:验收标准` 中补充 E-06 不可用时的降级路径 AC，覆盖"仅使用手工字段评分 + 界面提示准确度受限"的预期结果 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 在 `lead-intake/README.md:用户故事` 中区分手工提交与 E-07 自动汇入两条录入路径，在验收标准中补充批量自动汇入命中重复记录时的 AC | 产品负责人 | P2 | 待处理 |
| ACT-06 | F-06 | 修改 `lead-governance/README.md:业务场景` 场景一步骤 5 的表述，将"将其流转至指定销售"改为"生成分配推荐供管理者确认"，消除与 BR-04 的语义歧义 | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-07 | 在 `lead-assignment/README.md:业务对象定义` 中补充"分配池"业务说明，或在 BR-02 中以更直接的表述替代该术语 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 lead-intake, F-02 lead-scoring, F-03 lead-assignment, F-05 scoring-rule-mgmt；F-04 待创建，已在 R1 中记录）
- [x] R1 Feature 覆盖完备性检查已执行（双向比对 Epic 功能特性表与实际目录；F-04 无文档已记录为 F-01 一般发现）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：业务定义细化 ✓、Epic BR 引用正确性 ✓、场景步骤到 US 映射 ✓、DEP/ASM 承接——发现 DEP-03 未正式引用，记录为 F-02 一般发现）
- [x] R3 用户故事完备性检查已执行（场景步骤覆盖逐条比对、US-AC 双向追溯验证 ✓、角色一致性 ✓；发现 F-03 缺少场景三步骤 2 覆盖，记录为 F-03 一般发现；F-01 缺少自动汇入路径，记录为 F-05 建议发现）
- [x] R4 BR 引用一致性检查已执行（共享 BR 引用格式核验 ✓、Feature BR 无矛盾 ✓、"是否成立"类 BR 四要素完整性 ✓、局部编号唯一性 ✓；无新增发现）
- [x] R5 业务对象协调性检查已执行（跨 Feature 同名对象比对 ✓、状态名称一致性 ✓、BR 属性引用闭合 ✓、业务语义层保持 ✓；"分配池"悬空概念记录为 F-07 建议发现）
- [x] R6 验收标准协调性检查已执行（跨 Feature 冗余与矛盾检查 ✓、三路径覆盖度检查 ✓、AC 引用 BR 闭合 ✓、三要素完整性 ✓；F-02 降级路径 AC 缺失记录为 F-04 一般发现）
- [x] R7 跨 Feature 一致性检查已执行（角色命名一致性 ✓、跨 Feature 引用对称性 ✓、范围边界无交叉 ✓、NFR 承接完整性 ✓；场景一步骤 5 语义歧义记录为 F-06 建议发现）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议，指明目标文件与章节
- [x] 审核结论与问题统计数据一致（严重 0 / 一般 4 / 建议 3，结论为有条件通过）
- [x] 改进事项已为每条严重/一般级别的发现（F-01 至 F-04）创建对应 Action（ACT-01 至 ACT-04）
