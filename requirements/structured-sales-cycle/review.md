---
description: "Theme Review（主题审核记录）——审查「营销过程闭环」主题下全部 7 个史诗定义的完备性、协调性与一致性"
title: "Theme Review - [T-01] 营销过程闭环 (Structured Sales Cycle)"
category: "Product Review"
version: "v1.0"
document_type: "theme-review"
author: "copilot"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Theme Review - [T-01] 营销过程闭环 (Structured Sales Cycle)

## 审核摘要 (Review Summary)

**审核范围：** Theme [T-01] 营销过程闭环 (Structured Sales Cycle)

**Theme 文档路径：** `requirements/structured-sales-cycle/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0302 需求主题定义 | `requirements/structured-sales-cycle/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/lead-governance/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/nurture-followup/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/opportunity-pipeline/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/winloss-retrospective/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/marketing-automation/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/tag-management/README.md` |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/data-integration/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 6 |
| 建议 | 3 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R2 | 一般 | 全部 7 个 Epic 文档：各 Epic 自检清单章节 | 全部 7 个 Epic 的自检清单中均未显式引用对应的 Theme 验收标准编号（OC-01 至 OC-09）。Epic 对 Theme OC 的承接关系仅能通过阅读正文推断（如 E-03 在价值预估中提及"支撑 T-01 OC-03"，其余多数 Epic 仅在业务场景中隐含覆盖），缺乏可追溯的正向映射，无法直接验证 Epic 交付是否满足 Theme 验收约束。 | 在各 Epic 自检清单末尾补充一条"本 Epic 明确承接的 Theme 验收标准（OC-XX）均已在业务场景、功能特性或业务规则中有具体体现"的映射清单或逐条声明，将 OC 编号显式关联至承接该 OC 的 Feature 或 BR，使 Theme-Epic OC 映射关系可直接核查。 |
| F-02 | R3 | 一般 | `requirements/structured-sales-cycle/README.md:概述.价值承诺` / 全部 7 个 Epic 文档：概述.价值预估章节 | Theme 价值承诺中"年化人力节省等效从 ¥0 提升至 ≥ ¥50 万（M12，T-01 贡献部分）"在全部 7 个 Epic 的价值预估章节中均未被显式承接，该 KPI 仅出现在 Theme KPI 贡献路径矩阵（汇总视图）中，且矩阵列中的贡献描述为定性文字（如"策略回流减少试错成本"），未提供等效工时或金额估算。Epic 层无法向上追溯验证该 KPI 目标的可达性，存在 Theme 顶层 KPI 落地路径断裂风险。 | 在主要贡献 Epic（E-02、E-05、E-07）的价值预估中补充对"年化人力节省 ≥ ¥50 万"的分担承接说明，给出各 Epic 可独立衡量的效率改善量化依据（如 E-02 节省人均跟进录入工时 N 小时/周、E-07 替代手工录入场景节省 M 人天/月等），并标注对 Theme KPI 的贡献部分，使该 KPI 的可达性有据可查。 |
| F-03 | R3 | 一般 | `requirements/structured-sales-cycle/nurture-followup/README.md:概述.价值预估` / `requirements/structured-sales-cycle/marketing-automation/README.md:概述.价值预估` / `requirements/structured-sales-cycle/data-integration/README.md:概述.价值预估` | "单次跟进备案 ≤ 30 分钟"这一 Theme KPI 在 E-02、E-05、E-07 三个 Epic 中均使用完全相同的改善区间（从 ≥ 3 小时/次降低至 ≤ 30 分钟/次）作为价值预估依据，缺乏各 Epic 独立可衡量的子指标口径说明（如 E-02 降低填写录入工时、E-05 减少重复触达操作次数、E-07 替代手工录入耗时），不同 Epic 对同一改善值的重复声明在加总解读时存在重复计算风险，也难以独立评估各 Epic 的实际效益贡献。 | 为 E-02、E-05、E-07 分别细化独立可衡量的效率 KPI 子指标，明确各 Epic 在整体工时压缩中的贡献路径，并括注对 Theme KPI"单次跟进备案 ≤ 30 分钟"的贡献比例，参照 Theme KPI 贡献路径矩阵中已有的职责划分。 |
| F-04 | R4 | 一般 | `requirements/structured-sales-cycle/README.md:用户旅程.MKT Leader 旅程` Mermaid 图节点 C | MKT Leader 用户旅程 Mermaid 图中，高意向线索路径节点 C 标注为"E-03: 分配销售负责人"，但线索分配功能明确归属于 E-01（F-03 线索分配与流转：按分级结果将高意向线索智能推荐路由至销售，支持管理者人工覆盖与再分配）。E-03 的核心职责为从已分配线索建立商机并推进阶段，不包含线索分配。此错误导致 E-01 的核心分配能力在主旅程中完全不可见，且可能引起下游研发对 E-01 与 E-03 范围边界的误解。 | 将 MKT Leader 旅程中节点 C 的 Epic 归属从 E-03 修正为 E-01（`C[E-01: 分配销售负责人]`）；同时在销售 Leader/执行层旅程的首节点处，考虑补充 E-01 分配通知与 E-03 商机创建之间的交接关系说明（可在跨 Epic 业务约束中添加一条），使两条旅程中 E-01 和 E-03 的边界清晰一致。 |
| F-05 | R2 | 一般 | `requirements/structured-sales-cycle/README.md:外部依赖概览` / `requirements/structured-sales-cycle/nurture-followup/README.md:约束与依赖` / `requirements/structured-sales-cycle/opportunity-pipeline/README.md:自检清单` | Theme 外部依赖概览中声明"T-02 营销自动化能力（规则引擎、标签体系）"影响 E-02（培育触达降级为纯人工模式），但 E-02 约束与依赖章节仅列有 DEP-01 至 DEP-05，未声明对 T-02 能力的正式依赖及降级说明。同样，E-03 自检清单注明"GC-01 由 T-02 E-01 在转商机评分的上游保障"，但该跨 Theme 依赖未在 E-03 约束与依赖章节建立正式 DEP 条目及降级策略（降级方案仅隐含于自检说明，非权威来源）。Theme 级外部依赖表中已标注的 Epic 级影响未被对应 Epic 文档完整纳管。 | 在 E-02 约束与依赖章节新增 DEP-06：声明 T-02 营销自动化能力（规则引擎、标签体系）对 E-02 的影响，并定义 T-02 未就绪时的降级方案（培育触达降级为纯人工模式，月均覆盖 100 家目标达成风险增大）。在 E-03 约束与依赖章节新增正式 DEP 条目：声明 T-02 E-01 AI 转商机合理性评分对 E-03 的影响，并定义降级方案（E-03 转商机门控降级为纯规则校验，不影响主流程）。两处 DEP 条目已有实质内容，仅需从自检清单或章节说明中迁移至约束与依赖的正式结构化位置。 |
| F-06 | R5 | 一般 | `requirements/structured-sales-cycle/data-integration/README.md:约束与依赖.DEP-02/DEP-03` / `requirements/structured-sales-cycle/nurture-followup/README.md:约束与依赖` / `requirements/structured-sales-cycle/tag-management/README.md:约束与依赖` | E-07 DEP-02 声明"自动接入的行为数据须按 E-02 定义的跟进记录格式写入"（即 E-07 是 E-02 的上游数据供给方），但 E-02 约束与依赖章节中未声明对 E-07 行为数据的依赖，E-02 的 DEP-01～DEP-05 仅涵盖 E-01/E-03/E-05/E-04 的跨 Epic 依赖，E-07 作为上游来源缺失。同理，E-07 DEP-03 声明向 E-06 供给行为特征数据驱动自动打标，但 E-06 约束与依赖章节（DEP-01～DEP-03）未对应声明对 E-07 的上游依赖，依赖的单向声明导致 E-02 和 E-06 对 E-07 就绪状态缺乏正式管控，下游降级方案不明确。 | 在 E-02 约束与依赖章节新增 DEP-06（或下一可用编号）：声明 E-07 数据接入与同步是 E-02 自动触达跟进记录的行为数据来源，E-07 未就绪时行为类自动跟进记录缺失，须由销售人工补录。在 E-06 约束与依赖章节新增 DEP-04（或下一可用编号）：声明 E-07 采集的渠道行为特征是 E-06 自动打标的数据来源之一，E-07 未就绪时行为来源维度的自动打标不可用，降级为人工打标。 |
| F-07 | R5 | 建议 | `requirements/structured-sales-cycle/lead-governance/README.md:业务场景` 场景一步骤 6、场景三步骤 4 | E-01 业务场景中在描述线索接收确认和再分配操作时使用角色名"销售"，而 E-02 至 E-07 及 Theme 用户旅程中统一使用"销售执行层"表达同一角色。跨 Epic 角色命名不一致，虽不影响功能范围理解，但会造成角色清单推导时的歧义，影响文档可读性与后续研发协同。 | 将 E-01 业务场景中的"销售"替换为"销售执行层"，与 Theme 用户旅程和其他 Epic 中的角色命名保持一致。可参考 E-01 自检清单中已列出"销售"的出处并逐处统一。 |
| F-08 | R6 | 建议 | `requirements/structured-sales-cycle/data-integration/README.md:功能特性表.F-03` / `requirements/structured-sales-cycle/README.md:用户旅程.跨 Epic 业务约束` | E-07 F-03 手动导入的范围说明中包含"去重提示"描述，而 Theme 用户旅程跨 Epic 业务约束已明确声明"E-07 渠道接入负责原始数据拉取与格式映射，E-01 负责映射后数据的去重校验与入池；两者不重复实现去重能力"。"去重提示"的表述与 E-01 承担的去重校验职责在语义上存在潜在边界歧义，可能引起下游研发将 E-07 理解为也实现了去重逻辑。 | 在 E-07 F-03 范围说明中将"去重提示"细化为"在字段映射预览阶段对可能重复的记录进行预检提示（非实际去重决策，实际去重校验由 E-01 F-01 统一执行）"，明确 E-07 仅做预检告知，消除与 E-01 去重职责的边界歧义。 |
| F-09 | R5 | 建议 | `requirements/structured-sales-cycle/data-integration/README.md:业务规则` | E-07 业务规则章节中 BR 编号存在断层：BR-01、BR-02、BR-03 之后直接跳至 BR-05、BR-06，BR-04 缺失，可能因版本迭代删除条目后未重新排列编号，导致文档内部编号不连续，降低可读性与引用可靠性。 | 确认 BR-04 是否为有意删除并补充说明（如"BR-04 已合并至 BR-03"），或将 BR-05、BR-06 重新排列为 BR-04、BR-05，保持编号连续性。如 E-07 文档有其他条目引用了原 BR-05/BR-06 编号（如 E-07 场景二步骤 1 引用 BR-05），需同步更新引用。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 产品负责人（修改全部 7 个 Epic 的自检清单，在各 Epic 补充 Theme OC 承接声明） | P1 | 待处理 |
| ACT-02 | F-02 | 产品负责人（修改 E-02、E-05、E-07 价值预估，补充年化人力节省 KPI 分担口径） | P1 | 待处理 |
| ACT-03 | F-03 | 产品负责人（修改 E-02、E-05、E-07 价值预估，为效率 KPI 细化独立子指标） | P1 | 待处理 |
| ACT-04 | F-04 | 产品负责人（修改 Theme README 用户旅程 Mermaid 图，将节点 C 归属从 E-03 修正为 E-01） | P1 | 待处理 |
| ACT-05 | F-05 | 产品负责人（修改 E-02 和 E-03 约束与依赖章节，补充 T-02 相关 DEP 条目） | P1 | 待处理 |
| ACT-06 | F-06 | 产品负责人（修改 E-02 约束与依赖，新增 E-07 上游依赖条目；修改 E-06 约束与依赖，新增 E-07 行为特征供给依赖条目） | P1 | 待处理 |
| ACT-07 | F-07 | 产品负责人（修改 E-01 业务场景，将"销售"统一替换为"销售执行层"） | P2 | 待处理 |
| ACT-08 | F-08 | 产品负责人（修改 E-07 F-03 范围说明，澄清去重提示与 E-01 去重校验的边界） | P2 | 待处理 |
| ACT-09 | F-09 | 产品负责人（修改 E-07 业务规则，确认或重排 BR 编号，消除 BR-04 缺失断层） | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Theme 文档（A0302）全文
- [x] 已读取该 Theme 下全部 Epic 文档（A0303）全文（E-01 至 E-07 共 7 份）
- [x] R1 Epic 覆盖完备性检查已执行
- [x] R2 向下拆分契约兑现检查已执行（5 条映射逐条核验）
- [x] R3 价值指标协调性检查已执行（KPI 覆盖、量级、口径）
- [x] R4 用户旅程覆盖度检查已执行
- [x] R5 跨 Epic 一致性检查已执行（角色、编号、依赖、范围）
- [x] R6 Feature 清单完备性检查已执行
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致
- [x] 改进事项已为每条一般/严重级别的发现创建 Action
