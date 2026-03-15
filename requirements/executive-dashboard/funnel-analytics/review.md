---
description: "Epic Review（史诗审核记录），记录对 E-01「销售漏斗全链路视图」及其全部下属特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-01] 销售漏斗全链路视图 (Funnel Analytics)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-01] 销售漏斗全链路视图 (Funnel Analytics)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-01] 销售漏斗全链路视图（所属 Theme：T-03 CEO 决策驾驶舱）

**Epic 文档路径：** `requirements/executive-dashboard/funnel-analytics/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/executive-dashboard/funnel-analytics/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/funnel-analytics/features/f01-funnel-visualization/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/funnel-analytics/features/f02-owner-filter/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/funnel-analytics/features/f03-stage-drilldown/README.md` |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 3 |
| 一般 | 7 |
| 建议 | 0 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R3 | 严重 | `README.md:业务场景 > 场景二 步骤 4` / `features/f03-stage-drilldown/README.md:特性概述` | Epic 场景二步骤 4 明确要求"系统展示该负责人商机在各阶段的停留时长分布与行业基准对比"，且该步骤归属 F-03（Epic 跨特性协同说明：步骤 3-4 依赖 F-03）。但 F-03 的范围边界（包含项）和用户故事均未覆盖"行业基准对比"能力；F-03 仅提供单条商机的当前阶段停留时长数值，未定义行业基准来源、计算方法及对比展示规则。该业务能力在全部三个 Feature 中均无承接，是 Epic 业务场景到 Feature 覆盖的实质性缺口。 | 在 `features/f03-stage-drilldown/README.md` 的"范围边界（包含项）"中补充"各阶段停留时长与行业基准的对比展示"，在用户故事章节增加对应 US（覆盖 CEO 查看停留时长行业基准对比的场景），并配套补充业务规则（定义行业基准数据来源与缺失时处理方式）和验收标准。若产品负责人判断该能力不属于 F-03，须修改 Epic 场景二步骤 4 的跨特性归属说明，并明确由哪个 Feature 承接。 |
| F-02 | R7 | 严重 | `README.md:非功能需求 NFR-01` / `features/f01-funnel-visualization/README.md:业务规则` / `features/f02-owner-filter/README.md:业务规则` / `features/f03-stage-drilldown/README.md:业务规则` | Epic NFR-01 要求漏斗数据刷新延迟 ≤ 1 小时，以确保 CEO 看到当日可信快照。但 F-01、F-02、F-03 的业务规则（BR）和验收标准（AC）章节均未承接该非功能约束，任何 Feature 均未定义数据时效性相关的判定规则或验收场景。下游 S0306 功能特性设计将缺乏数据刷新延迟的明确约束输入，可能导致实现阶段忽略该时效性要求。 | 在 `features/f01-funnel-visualization/README.md` 的业务规则章节补充"数据时效性"BR，引用 Epic NFR-01，明确"漏斗视图所展示的数据须基于刷新延迟 ≤ 1 小时的最新快照"；并在验收标准中增加对应 AC（例如：前置条件为最新快照距当前超过 1 小时，预期结果为视图显示数据时效提示或标注快照时间戳）。F-02 和 F-03 可在各自业务规则中通过"参见 F-01 数据时效性约束"或单独添加同等 BR 的方式承接该 NFR。 |
| F-03 | R7 | 严重 | `README.md:非功能需求 NFR-03` / `features/f01-funnel-visualization/README.md:业务规则` / `features/f02-owner-filter/README.md:业务规则` / `features/f03-stage-drilldown/README.md:业务规则` | Epic NFR-03 要求 CEO 对漏斗数据的查看与筛选操作须形成可审计的操作日志，满足 GC-04 操作审计约束。但 F-01、F-02、F-03 的业务规则和验收标准均未引入操作审计相关的 BR 或 AC；"管理员"或"审计员"等与审计能力相关的角色在任何 Feature 的用户故事中均未出现；"操作日志"概念在全部 Feature 定义中无一处提及。下游 S0306 设计无 GC-04 合规实现的需求输入。 | 在 F-01、F-02、F-03 各自的业务规则章节补充"操作审计"BR，引用 Epic NFR-03 及 GC-04，明确须生成审计日志的操作范围（如查看漏斗视图、切换时间窗口、筛选负责人、进入商机明细等），并在各 Feature 验收标准中增加对应 AC，验证上述操作产生可查询的审计记录。若操作审计由平台统一实现而非在各 Feature 单独定义，须在 F-01 中明确说明平台层承接机制，以保留对 GC-04 的可追溯性。 |
| F-04 | R4 | 一般 | `README.md:业务规则 BR-06` / `features/f02-owner-filter/README.md:特性概述 & 业务规则` / `features/f03-stage-drilldown/README.md:特性概述 & 业务规则` | Epic BR-06（阶段一致）要求漏斗各阶段名称与阶段划分标准与 T-01 商机推进保持一致，适用范围标注为 F-01、F-02、F-03。仅 F-01 业务规则（BR-01）正确引用了 Epic [BR-06]；F-02 特性概述约束引用列表和业务规则章节均未出现对 Epic [BR-06] 的引用；F-03 特性概述约束引用列表和业务规则章节亦未引用 Epic [BR-06]。F-02 按阶段展示各负责人转化率，F-03 以"当前阶段"为核心展示维度和业务对象属性，两者对阶段定义一致性的依赖与 F-01 同等重要，缺少显式引用将在设计与实现阶段造成遗漏风险。 | 在 `features/f02-owner-filter/README.md` 特性概述（业务定义段）中补充"漏斗阶段名称与划分须与 T-01 商机推进定义保持一致（参见 Epic [BR-06]）"；在 `features/f03-stage-drilldown/README.md` 特性概述（业务定义段）中同样补充对 Epic [BR-06] 的引用。 |
| F-05 | R4 | 一般 | `README.md:业务规则 BR-04` / `features/f01-funnel-visualization/README.md:特性概述 & 业务规则` / `features/f02-owner-filter/README.md:业务规则 BR-02` | Epic BR-04（口径统一，标注 [推导-待确认]）声称跟进及时率计算口径须在 F-01 全链路视图与 F-02 负责人视图中统一。但 F-01 的范围边界（包含项）、用户故事和全部业务规则中均不涉及"跟进及时率"——F-01 的展示内容限于各阶段数量、转化率与停留时长，未有任何跟进及时率相关定义。F-02 BR-02 声称跟进及时率时间窗口阈值"与 F-01 中使用的口径完全一致（参见 Epic [BR-04]）"，形成对 F-01 中不存在内容的悬空引用；设计与测试阶段无法从 F-01 中找到该口径定义的来源。 | 由产品负责人确认 F-01 是否需要展示跟进及时率指标。若是，须在 F-01 范围边界（包含项）中补充该能力，并增加对应 US/BR/AC；若否，须将 Epic BR-04 适用范围中的 F-01 修正为仅 F-02，并将 F-02 BR-02 的引用描述改为"跟进及时率口径由本特性（F-02）统一定义，参见 Epic [BR-04]"，消除对 F-01 的悬空引用。 |
| F-06 | R4 | 一般 | `README.md:业务规则 BR-03` / `features/f02-owner-filter/README.md:特性概述 & 业务规则` | Epic BR-03（停滞对齐）要求阶段停留时长的起止边界定义须与 E-03 商机健康度预警完全一致，适用范围标注为 F-01、F-02、F-03。F-01（BR-04）和 F-03（BR-03）均正确引用了 Epic [BR-03]；但 F-02 特性概述约束引用列表（仅含 Epic [BR-02]、[BR-04]、[BR-05]）及全部业务规则中均未引用 Epic [BR-03]，且 F-02 的"负责人漏斗快照"业务对象定义中无"停留时长"属性，表明 F-02 当前未定义任何停留时长相关数据。此处存在两种可能的问题：一是 Epic BR-03 对 F-02 的适用范围声明过宽（F-02 实际不涉及停留时长）；二是 F-02 本应提供负责人维度的停留时长汇总但存在功能遗漏。 | 由产品负责人明确 F-02 是否需要展示负责人维度的停留时长相关数据。若确认不涉及，须将 Epic BR-03 的适用范围从 F-01/F-02/F-03 修正为 F-01/F-03，确保 Epic 约束范围声明与实际 Feature 覆盖一致；若确认 F-02 需展示停留时长，须在 F-02 业务对象定义中补充相关属性，并在业务规则和特性概述中补充对 Epic [BR-03] 的引用。 |
| F-07 | R7 | 一般 | `features/f03-stage-drilldown/README.md:特性概述（业务定义）` / `features/f02-owner-filter/README.md:特性概述（范围边界）` | F-03 特性概述明确声明"本特性以 F-01 全链路漏斗可视化为前提（参见 Epic [INT-01]）"，但 F-02 的范围边界显式声明"从漏斗阶段进入商机明细列表由 F-03 承接"，Epic 场景二步骤 3 亦将"从负责人视图下钻至商机明细"归属于 F-03。依赖对称性要求：若 F-02 提供了通向 F-03 的入口，则 F-03 须声明对该入口的承接。当前 F-03 仅声明从 F-01 阶段视图进入，未定义从 F-02 负责人视图进入的路径，该 CEO 操作路径在 F-03 用户故事中无对应 US 覆盖（场景二步骤 3 的"从负责人视图下钻"无 US 可追溯）。 | 在 `features/f03-stage-drilldown/README.md` 特性概述（业务定义段或范围边界）中补充"亦可从 F-02 按负责人筛选视图中的特定阶段进入同一商机明细列表"；在用户故事章节补充对应 US，覆盖 CEO 从 F-02 视图发起下钻的操作路径，并配套增加 AC；同时在约束引用中注明 F-02 为本特性的可选上游入口（弱依赖，不影响 INT-01 的强依赖关系）。 |
| F-08 | R5 | 一般 | `features/f03-stage-drilldown/README.md:业务对象定义 > 阶段商机明细记录` / `features/f03-stage-drilldown/README.md:业务规则 BR-03、BR-05` | F-03 业务对象"阶段商机明细记录"的属性表包含"商机名称、负责人、当前阶段、当前阶段停留时长、最近跟进时间"五项属性，未声明"进入阶段时间点"属性。但 BR-03 停留时长计算公式为"查询时间点 − 商机进入该阶段的时间点"，BR-05 排序规则将"商机进入该阶段的时间点"作为同一停留时长下的次级排序键，两条业务规则均将该属性作为计算或排序依据，造成业务规则引用了业务对象定义中未声明的属性，BR 与业务对象定义之间存在不一致。 | 在 `features/f03-stage-drilldown/README.md` 的"阶段商机明细记录"属性表中补充"进入阶段时间点"属性，业务说明可为："商机进入当前阶段的时间戳，用于计算当前阶段停留时长，以及作为停留时长相同时的次级排序依据"。 |
| F-09 | R6 | 一般 | `features/f03-stage-drilldown/README.md:用户故事 US-04` / `features/f03-stage-drilldown/README.md:验收标准 AC-05` | F-03 US-04 明确要求"在商机明细列表中按停留时长排序（从长到短或从短到长）"，显式声明了升序与降序两个方向均为用户故事覆盖范围。但 AC-05 仅定义"降序排序"（从长到短）的验收场景，缺少"升序排序"（从短到长）的验收标准；US-04 声明的升序操作路径无对应 AC 可追溯，该路径缺乏测试依据。 | 在 `features/f03-stage-drilldown/README.md` 验收标准章节补充升序排序验收标准（可作为新 AC-06 或扩充 AC-05）：前置条件为 CEO 处于商机明细列表，触发动作为 CEO 选择按停留时长升序排序，预期结果为列表按停留时长由短到长重新排列，停留时长相同时按商机进入该阶段时间点早者优先（参见 BR-05）；并在 US-04 的 AC Ref 中补充该新 AC 编号。 |
| F-10 | R7 | 一般 | `README.md:非功能需求 NFR-02` / `features/f01-funnel-visualization/README.md:用户故事 & 验收标准` | Epic NFR-02 要求漏斗指标口径支持管理员配置、关键指标提供下钻路径以满足 GC-02 数据主权约束。但 F-01、F-02、F-03 的用户故事和验收标准中均无"管理员"角色相关的 US 或 AC；"管理员可配置关键指标口径"的能力未被任何 Feature 的范围边界（包含项）声明，也无 BR 或 AC 覆盖该配置交互。下游 S0306 对此能力的设计无需求输入，GC-02 合规路径不可追溯。 | 在 F-01 特性概述的范围边界中补充"指标口径配置"或在用户故事章节增加"管理员"角色的 US（如：As a 管理员，I want to configure the calculation parameters for key funnel metrics），并增加对应验收标准。若该配置能力归属于独立的系统管理 Feature 或平台级配置模块，须在 Epic 约束与依赖中明确说明，并由产品负责人指定其归属 Feature。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 在 `features/f03-stage-drilldown/README.md` 范围边界（包含项）中补充"行业基准对比"能力，并增加对应 US、BR（含行业基准来源与缺失处理）、AC；或修改 Epic 场景二步骤 4 的跨特性归属声明，明确该能力的承接 Feature | 产品负责人 | P0 | 待处理 |
| ACT-02 | F-02 | 在 F-01 业务规则章节补充"数据时效性"BR（漏斗数据刷新延迟 ≤ 1 小时，引用 Epic NFR-01），并增加对应 AC；F-02 和 F-03 以引用或独立 BR 方式同步承接该约束 | 产品负责人 | P0 | 待处理 |
| ACT-03 | F-03 | 在 F-01、F-02、F-03 各自的业务规则章节补充"操作审计"BR（引用 Epic NFR-03 / GC-04），明确须生成审计日志的操作范围，并在各 Feature 验收标准中增加对应 AC | 产品负责人 | P0 | 待处理 |
| ACT-04 | F-04 | 在 `features/f02-owner-filter/README.md` 和 `features/f03-stage-drilldown/README.md` 的特性概述（业务定义段）中分别补充对 Epic [BR-06]（阶段一致）的引用声明 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 由产品负责人确认 Epic BR-04 中 F-01 的适用性：若 F-01 不涉及跟进及时率，则修正 Epic BR-04 适用范围并将 F-02 BR-02 的引用改为指向 F-02 自身定义，消除悬空引用；若 F-01 需包含跟进及时率，则在 F-01 中补充对应 US/BR/AC | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-06 | 由产品负责人确认 F-02 是否展示停留时长相关数据：若否，修正 Epic BR-03 适用范围（移除 F-02）；若是，在 `features/f02-owner-filter/README.md` 业务对象和特性概述中补充相关属性与 Epic [BR-03] 引用 | 产品负责人 | P1 | 待处理 |
| ACT-07 | F-07 | 在 `features/f03-stage-drilldown/README.md` 特性概述中补充 F-02 作为上游入口的说明，并增加从 F-02 视图进入商机明细的 US 和对应 AC | 产品负责人 | P1 | 待处理 |
| ACT-08 | F-08 | 在 `features/f03-stage-drilldown/README.md` 业务对象"阶段商机明细记录"属性表中补充"进入阶段时间点"属性及业务说明 | 产品负责人 | P1 | 待处理 |
| ACT-09 | F-09 | 在 `features/f03-stage-drilldown/README.md` 验收标准章节补充升序排序验收标准（覆盖 US-04 的"从短到长"路径），并在 US-04 的 AC Ref 中补充新 AC 编号 | 产品负责人 | P1 | 待处理 |
| ACT-10 | F-10 | 在 F-01 或指定归属 Feature 中补充"管理员"角色的指标口径配置 US 和验收标准，承接 Epic NFR-02（GC-02 数据主权）；若由平台统一实现，须在 Epic 约束与依赖中明确说明 | 产品负责人 | P1 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01、F-02、F-03）
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
