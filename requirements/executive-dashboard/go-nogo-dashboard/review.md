---
description: "Epic Review（史诗审核记录），记录对 E-04 规则效果验收看板全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-04] 规则效果验收看板 (Rule Performance Go/No-Go Dashboard)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
task_id: "101514"
sprint: "20260309"
---

# Epic Review - [E-04] 规则效果验收看板 (Rule Performance Go/No-Go Dashboard)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-04] 规则效果验收看板（所属 Theme: T-03 CEO 决策驾驶舱）

**Epic 文档路径：** `requirements/executive-dashboard/go-nogo-dashboard/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/executive-dashboard/go-nogo-dashboard/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/go-nogo-dashboard/kpi-tracking-dashboard/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/go-nogo-dashboard/rule-version-comparison/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/go-nogo-dashboard/historical-trend-analysis/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/go-nogo-dashboard/go-nogo-decision/README.md` |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 1 |
| 一般 | 7 |
| 建议 | 1 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R2 | 一般 | `kpi-tracking-dashboard/README.md:业务规则`（及 F-02、F-03、F-04 同章节） | Epic 约束与依赖章节定义了 6 项 DEP 和 1 项 ASM，但四个 Feature 的业务规则均未以 "参见 Epic [DEP-xx]" 或 "参见 Epic [ASM-xx]" 形式承接。关键缺失：(1) ASM-01 对 F-01/F-02/F-03 有直接降级影响，无任何 Feature 引用；(2) DEP-03/DEP-04（T-01 版本库接口依赖）对 F-02/F-03/F-04 均有依赖，同样无显式引用 | 在 F-01/F-02/F-03 的业务规则中补充对 ASM-01 的引用并注明降级策略；在 F-02/F-03/F-04 的相关 BR 中补充对 DEP-03、DEP-04 的引用，确保上游约束在 Feature 层不丢失 |
| F-02 | R4 | 一般 | `kpi-tracking-dashboard/README.md:业务规则` | F-01（kpi-tracking-dashboard）在业务对象定义中明确"活跃版本号来源于 T-01/E-01 F-05 或 T-01/E-05 F-01"，其 BR-02 也要求"在显著位置展示当前活跃规则版本号与生效日期"；上述行为直接对应 Epic BR-01（版本只读引用："规则版本信息须且仅从 T-01 版本库引用，E-04 不得创建或修改规则版本内容"），但 F-01 的全部 5 条业务规则中均无 "参见 Epic [BR-01]" 引用。Epic BR-01 已在 F-02（BR-04）、F-03（BR-03）中被引用，唯 F-01 缺失 | 在 F-01 业务规则中补充对 Epic BR-01 的引用，例如将 BR-02 扩展为"须在显著位置展示当前活跃规则版本号与生效日期（参见 Epic [BR-01]：版本信息只读引用，来源于 T-01/E-01 F-05 或 T-01/E-05 F-01，本特性不创建或修改任何规则版本内容）" |
| F-03 | R4 | 一般 | `go-nogo-decision/README.md:业务规则 BR-07`、`go-nogo-decision/README.md:验收标准 AC-06` | F-04（go-nogo-decision）US-03、BR-07 及 AC-06 定义了 Go 决策后可选的星标更新操作，AC-06 也描述了"当前版本成为星标，旧星标自动取消"的行为；此行为与 Epic BR-03（星标唯一性：同一规则类型同一时刻仅一个星标，新标记时旧星标自动取消）和 Epic BR-04（星标可变更：MKT Leader 可随时标记任意已发布版本为星标）直接相关，但 F-04 的 BR-07 未引用 Epic BR-03 和 Epic BR-04，导致 F-04 中的星标更新操作与 F-02 中的星标管理约束基准缺乏一致的规则来源 | 在 F-04（go-nogo-decision）BR-07 中增加对 Epic BR-03 和 Epic BR-04 的引用，明确 Go 后星标更新操作同样遵循 Epic 层定义的星标唯一性与可变更约束，与 F-02 的星标管理保持规则一致性 |
| F-04 | R4 | 严重 | `go-nogo-decision/README.md:业务规则 BR-06`、`go-nogo-decision/README.md:验收标准 AC-05`、`go-nogo-decision/README.md:业务对象定义 - 回退执行状态` | F-04 BR-06 仅定义了"系统须自动向上游发起版本切换请求，将规则切回至当前星标版本"的成功路径；业务对象"Go/No-Go 决策记录"的"回退执行状态"属性包含"回退失败"值（标注 [推导-待确认]），表明团队已识别失败可能性，但全部业务规则中无任何一条 BR 定义上游版本切换请求失败时的系统处置规则（如失败后是否重试、如何提示用户、审计日志如何记录失败状态），AC-05 也仅覆盖成功路径。当 No-Go 决策已写入不可篡改审计日志但上游版本切换实际未生效时，系统将处于决策记录与规则实际状态不一致的状态，下游 S0306 设计无法实现完整 No-Go 流程，亦无法定义失败场景的用户交互与容错逻辑 | 在 F-04 业务规则中补充 BR（或扩展 BR-06），定义上游版本切换失败的处置规则，至少明确：(1) 审计日志中"回退执行状态"应记录失败状态；(2) 是否支持重试及重试策略；(3) 失败时向 MKT Leader 展示的错误提示内容；同步在验收标准中补充失败路径 AC（前置条件：MKT Leader 确认 No-Go 回退，上游返回失败响应；预期结果：审计日志记录失败状态，MKT Leader 收到失败提示并知悉规则未被切换） |
| F-05 | R5 | 一般 | `rule-version-comparison/README.md:业务对象定义 - 版本对比快照` | "版本对比快照"业务对象包含"数据引用期次"属性，定义为"对比数据所对应的统计期次标识，确保数据来源可溯"；但 F-02 全部业务规则与用户故事中均无对应的 BR 定义该期次的确定方法。KPI 对比使用哪个期次的数据（活跃版本的最近完整统计周期、观察期内累计数据、还是系统默认最新可用期次）在 Feature 定义层面存在歧义，导致下游 S0306 设计无法明确活跃版本与星标版本的数据对齐逻辑，可能产生因期次不一致而失真的对比结果 | 在 F-02 业务规则中补充 BR 明确"版本对比快照"数据期次的确定规则（建议表述为：活跃版本与星标版本各自取相同统计期次的最近完整周期数据进行对比，若某版本在该期次无数据则提示"无可用对比数据"）；同步在 AC 中增加对应验收标准，验证对比视图明确标注所展示数据的统计期次 |
| F-06 | R6 | 一般 | `historical-trend-analysis/README.md:业务规则 BR-06`、`historical-trend-analysis/README.md:验收标准` | F-03 BR-06 明确定义了查询时段超出 36 个月留存边界时的展示行为："边界内数据正常呈现，超出部分须以明确的不可用提示标注"；但 F-03 全部 7 条验收标准（AC-01 至 AC-07）均未覆盖该边界条件场景，下游 S0306 设计缺少对应的用户交互与提示样式验收基准 | 在 F-03 验收标准中补充 AC：前置条件为 MKT Leader 指定的查询时段（起止日期范围）跨越 36 个月留存边界；触发动作为 MKT Leader 提交查询；预期结果为 36 个月内的数据正常展示，超出边界部分明确标注不可用提示，且不影响边界内数据的正常呈现（落实 BR-06） |
| F-07 | R6 | 一般 | `go-nogo-decision/README.md:业务规则`、`rule-version-comparison/README.md:业务规则 BR-07` | Epic NFR-02 要求"星标变更、Go/No-Go 决策及回退操作日志完整保存，支持审计导出"；F-04 承担全部 Go/No-Go 决策与回退的审计日志写入职责，F-02 BR-07 承担星标变更的审计日志写入职责，但两个 Feature 的全部验收标准均未定义审计日志导出能力的验收场景，"支持审计导出"在 Feature 层无可验收的行为定义，下游无法基于现有 Feature 定义实现该 NFR | 明确"审计导出"能力的归属 Feature（建议作为 F-04 的新增 US 或单独在 Epic 约束中标注由外部治理模块 GC-04 实现），并补充对应 US 与 AC，验证"MKT Leader 或 CEO 可按操作类型、时间范围、操作人等条件筛选并导出审计日志"（落实 Epic NFR-02） |
| F-08 | R6 | 一般 | `kpi-tracking-dashboard/README.md:验收标准`、`rule-version-comparison/README.md:验收标准`、`historical-trend-analysis/README.md:验收标准` | Epic NFR-03 要求"T-03/E-01 与 T-03/E-02 源数据完成刷新后，E-04 看板同步延迟 ≤ 5 分钟"；F-01、F-02、F-03 作为数据展示特性，直接依赖该同步时效，但三个 Feature 的全部验收标准均未覆盖上游数据刷新触发后的同步延迟行为，亦未定义同步超时或同步失败时的降级展示策略，NFR-03 缺乏可验收的行为定义 | 在 F-01（或 F-03）验收标准中补充 AC：前置条件为 T-03/E-01 或 T-03/E-02 完成一次数据刷新；预期结果为 E-04 相关看板在 5 分钟内自动同步展示最新数据（落实 Epic NFR-03）；并补充降级路径 AC：当同步超时或失败时，看板展示上次成功同步的数据并标注刷新时间戳，不对 MKT Leader 静默失败 |
| F-09 | R7 | 建议 | `kpi-tracking-dashboard/README.md:业务规则 BR-04`、`historical-trend-analysis/README.md:业务规则 BR-04` | F-01（kpi-tracking-dashboard）BR-04 定义默认时间粒度为月（[推导-待确认]），F-03（historical-trend-analysis）BR-04 定义默认时间粒度为周（[推导-待确认]），同属 E-04 的两个数据看板特性默认粒度设置不一致，且两处均为推导值，缺少差异化理由说明，存在用户在特性间切换时产生认知不一致的风险 | 在 F-01 BR-04 或 F-03 BR-04 中补充差异化理由注释（如：F-01 聚焦当期规则运行效果监控，月粒度有利于减少短期波动干扰；F-03 聚焦历史走势归因，周粒度有利于精确定位版本切换后的效果拐点），或通过产品确认将两者统一，消除认知不一致风险 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-04 | 在 `go-nogo-decision/README.md:业务规则` 中补充 BR（或扩展 BR-06），定义上游版本切换请求失败时的系统处置规则（审计记录失败状态、重试策略、用户提示内容）；同步在 `go-nogo-decision/README.md:验收标准` 中补充失败路径 AC | 产品负责人（执行 S0304 修订） | P0 | 待处理 |
| ACT-02 | F-01 | 在 `kpi-tracking-dashboard/README.md`、`rule-version-comparison/README.md`、`historical-trend-analysis/README.md`、`go-nogo-decision/README.md` 的业务规则章节中，分别补充对 Epic ASM-01 的引用；在 F-02、F-03、F-04 的相关 BR 中补充对 Epic DEP-03、DEP-04 的引用 | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-03 | F-02 | 在 `kpi-tracking-dashboard/README.md:业务规则` 中补充对 Epic BR-01 的引用（版本只读引用），与 F-02 BR-04、F-03 BR-03 保持一致 | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-04 | F-03 | 在 `go-nogo-decision/README.md:业务规则 BR-07` 中增加对 Epic BR-03（星标唯一性）和 Epic BR-04（星标可变更）的引用，确保 F-04 Go 后的星标更新遵循与 F-02 一致的约束基准 | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-05 | F-05 | 在 `rule-version-comparison/README.md:业务规则` 中补充 BR，定义"版本对比快照"所用数据期次的确定规则；同步在 `rule-version-comparison/README.md:验收标准` 中补充对应 AC | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-06 | F-06 | 在 `historical-trend-analysis/README.md:验收标准` 中补充 36 个月留存边界条件 AC（落实 BR-06） | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-07 | F-07 | 明确"审计导出"能力的归属 Feature，在对应 Feature 中补充 US 与 AC（落实 Epic NFR-02） | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-08 | F-08 | 在 `kpi-tracking-dashboard/README.md:验收标准` 或 `historical-trend-analysis/README.md:验收标准` 中补充数据同步延迟 ≤ 5 分钟的 AC 及降级路径 AC（落实 Epic NFR-03） | 产品负责人（执行 S0304 修订） | P1 | 待处理 |
| ACT-09 | F-09 | 在 `kpi-tracking-dashboard/README.md:业务规则 BR-04` 或 `historical-trend-analysis/README.md:业务规则 BR-04` 中补充默认粒度差异化理由，或通过产品确认统一两者默认粒度 | 产品负责人（执行 S0304 修订） | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 kpi-tracking-dashboard、F-02 rule-version-comparison、F-03 historical-trend-analysis、F-04 go-nogo-decision）
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
