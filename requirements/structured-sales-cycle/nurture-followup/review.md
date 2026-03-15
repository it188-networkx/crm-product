---
description: "Epic Review（史诗审核记录）——培育与跟进沉淀，记录对 E-02 及其全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-02] 培育与跟进沉淀 (Nurture & Follow-up)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-18"
last_updated: "2026-03-18"
status: "审核完成"
---

# Epic Review - [E-02] 培育与跟进沉淀 (Nurture & Follow-up)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-02] 培育与跟进沉淀（所属 Theme: [T-01] 结构化销售过程）

**Epic 文档路径：** `requirements/structured-sales-cycle/nurture-followup/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/nurture-followup/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/nurture-followup/followup-rhythm-plan/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/nurture-followup/structured-followup-record/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/nurture-followup/customer-followup-timeline/README.md` |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 1 |
| 一般 | 4 |
| 建议 | 3 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 严重 | `nurture-followup/README.md:功能特性` | Epic 功能特性表中 Feature [F-04] 跟进提醒与待办（P1）的关联文档列标注为"待创建"，对应子目录 `followup-rhythm-plan/`（F-01）、`structured-followup-record/`（F-02）、`customer-followup-timeline/`（F-03）均已存在文档，而 F-04 既无目录也无 README.md。Epic 业务场景一步骤 2（"销售在当日任务视图中查看待跟进客户列表"）、Epic BR-07（"跨来源提醒消重"）均依赖 F-04 承接，当前无文档导致该能力无 US/AC/BR 覆盖，构成悬空 Feature 引用。 | 为 F-04 创建 `nurture-followup/followup-reminder-todo/README.md`，按 S0304 完成特性定义，覆盖到期/逾期提醒推送、提醒关联节奏计划、逾期标记及 Epic BR-07 跨来源提醒消重逻辑；完成后将 Epic 功能特性表中 F-04 的关联文档链接更新为实际路径。 |
| F-02 | R3 | 一般 | `followup-rhythm-plan/README.md:用户故事` | F-01 用户故事表中 US-01 的 AC Ref 仅列 AC-01、AC-02，但验收标准表中 AC-07（"客户类型标注缺失时系统按终端客户默认节奏生成计划"）的 US Ref 标注为 US-01。US-01 侧缺少 AC-07 引用，双向追溯断链：US-01 无法直接导航到其对应的类型缺省场景 AC，违反 R3 要求的 US→AC 双向可追溯。 | 将 `followup-rhythm-plan/README.md` 中 US-01 的 AC Ref 由 `AC-01, AC-02` 修改为 `AC-01, AC-02, AC-07`，使 US-01 与 AC-07 的双向引用闭合一致。 |
| F-03 | R3 | 一般 | `customer-followup-timeline/README.md:用户故事` | F-03 用户故事表中存在两处双向追溯断链：（1）US-01 的 AC Ref 仅列 AC-01、AC-02，但 AC-06（"200 条记录性能验收"）的 US Ref 标注为 US-01、US-04，且 AC-07（"时间线不提供删除入口"）的 US Ref 标注为 US-01，两者均未出现在 US-01 的 AC Ref 中；（2）US-04 的 AC Ref 仅列 AC-05，但 AC-06 的 US Ref 包含 US-04，US-04 侧缺少 AC-06 引用。文档自检清单中已声明"US-04→AC-05/06"，与实际表格不符，自检结论与文档内容矛盾。 | 将 `customer-followup-timeline/README.md` 中 US-01 的 AC Ref 修改为 `AC-01, AC-02, AC-06, AC-07`；US-04 的 AC Ref 修改为 `AC-05, AC-06`，使所有双向引用闭合，并更正自检清单中的 US Ref 声明。 |
| F-04 | R7 | 一般 | `followup-rhythm-plan/README.md:业务对象定义` / `structured-followup-record/README.md:业务对象定义` | F-01 与 F-02 之间存在未建模的跨 Feature 触发依赖：F-01 业务对象"跟进节奏计划"定义了属性"下次跟进建议时间"，其说明为"基于上次跟进完成时间与当前节奏间隔推算的下一次建议触达时间"，隐含的含义是每次 F-02 完成跟进记录归档后须触发 F-01 的节奏计划重算。但 F-01 和 F-02 的 US/AC/BR 均未声明此跨 Feature 触发关系：F-01 无"跟进记录完成后节奏计划自动更新下次跟进时间"的 AC，F-02 亦未在范围边界中声明"归档完成后触发 F-01 节奏计划更新"的输出依赖。在下游 S0306 设计阶段，此缺口将造成实现边界模糊。 | 在 `followup-rhythm-plan/README.md:验收标准` 中补充 AC："前置条件：销售已提交跟进记录且 F-02 归档完成；触发动作：系统重算节奏计划下次跟进建议时间；预期结果：节奏计划的'下次跟进建议时间'更新为本次完成时间加当前节奏间隔"，并在 `followup-rhythm-plan/README.md:特性概述:范围边界` 的外部依赖中声明"依赖 F-02 跟进记录归档完成事件驱动下次跟进建议时间重算"。 |
| F-05 | R7 | 一般 | `nurture-followup/README.md:非功能需求` / `followup-rhythm-plan/README.md:验收标准` / `structured-followup-record/README.md:验收标准` / `customer-followup-timeline/README.md:验收标准` | Epic NFR-03 要求"跟进记录新增、修正，节奏计划变更，责任人更换操作均须留存完整审计日志，支持按客户 ID、操作人、时间范围检索"。当前 F-01 的 BR-03 和 AC-06 承接了"节奏变更审计留存"和"责任人变更审计记录"，但"按客户 ID、操作人、时间范围检索审计日志"的可检索性约束，以及"跟进记录新增与修正的审计日志"的检索能力，在现有三个 Feature 的 AC 中均无对应验收场景覆盖。NFR-03 的检索维度要求处于未承接状态。 | 在 `structured-followup-record/README.md:验收标准` 中补充 AC，覆盖"跟进记录新增与修正审计日志可按客户 ID、操作人、时间范围检索"的场景；在 `followup-rhythm-plan/README.md:验收标准` 中补充 AC，覆盖"节奏变更与责任人变更审计日志可按上述三个维度检索"的场景；确保两个 Feature 的 BR 中明确引用 Epic NFR-03。 |
| F-06 | R4 | 建议 | `customer-followup-timeline/README.md:业务规则` | F-03 BR-02（"时间线不可过滤删除"）约束内容为"时间线须全量呈现 F-02 归档的所有跟进记录，不得因来源类型、记录人或意向等级而隐藏任何已归档记录"，其语义来源于 Epic BR-03（"记录不可删除"）在展示层的延伸应用。BR-02 正文未显式引用 `参见 Epic [BR-03]`，仅在 AC-07 的注脚中以"原始记录不可删除由 F-02 BR-01 保障"间接说明。与 F-02 BR-01 显式标注"参见 Epic [BR-03]"的做法不一致，跨 Feature 的规则溯源路径不统一。 | 在 `customer-followup-timeline/README.md:业务规则` 的 BR-02 定义开头添加"参见 Epic [BR-03]"引用，与 F-02 BR-01 的引用格式保持一致，明确该约束的 Epic 级权威来源。 |
| F-07 | R5 | 建议 | `structured-followup-record/README.md:业务对象定义` / `customer-followup-timeline/README.md:业务对象定义` | 跨 Feature 业务对象属性命名不一致：F-02 "跟进记录"业务对象中，标识记录是人工创建还是自动触达的属性名为"创建类型"；F-03 "时间线事件"业务对象中，描述相同业务语义的属性名为"来源类型"。两者均使用"人工跟进/自动触达"作为枚举值，指代完全相同的业务概念，但属性名称不同。下游设计阶段可能导致同一业务字段在两个模块使用不同命名而造成混淆。 | 统一两处属性命名，建议在 `customer-followup-timeline/README.md:业务对象定义` 中将"来源类型"修改为"创建类型"（以 F-02 为权威来源），并在 F-03 相关 BR 和 AC 中同步更新属性名称引用。 |
| F-08 | R6 | 建议 | `structured-followup-record/README.md:验收标准` / `customer-followup-timeline/README.md:验收标准` | F-02 AC-06（"销售尝试删除已提交的跟进记录，操作被拒绝"）与 F-03 AC-07（"销售尝试在时间线视图中删除某条历史跟进记录，操作被拒绝"）在两个不同 Feature 中均定义了"记录不可删除"的验收场景，业务规则来源相同（均源自 Epic BR-03）。虽然触发入口不同（记录管理视图 vs 时间线视图），但预期结果完全相同，存在跨 Feature 冗余定义，维护两处时存在结论分叉风险。 | 将"记录不可删除"的权威验收场景归属 F-02（F-02 AC-06），F-03 AC-07 修改为前置条件引用 F-02 AC-06，或将 F-03 AC-07 的描述聚焦于"时间线视图不提供删除入口"这一 UI 层约束，明确与 F-02 AC-06 的层次差异，避免规则重复。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 创建 `requirements/structured-sales-cycle/nurture-followup/followup-reminder-todo/README.md`，按 S0304 完成 F-04 跟进提醒与待办的特性定义，覆盖 Epic 场景一步骤 2 的待跟进任务视图、Epic BR-07 跨来源提醒消重逻辑；更新 Epic 功能特性表中 F-04 关联文档链接 | 产品负责人 | P0 | 待处理 |
| ACT-02 | F-02 | 将 `followup-rhythm-plan/README.md:用户故事` 中 US-01 的 AC Ref 由 `AC-01, AC-02` 修改为 `AC-01, AC-02, AC-07`，闭合双向追溯 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-03 | 将 `customer-followup-timeline/README.md:用户故事` 中 US-01 的 AC Ref 修改为 `AC-01, AC-02, AC-06, AC-07`；US-04 的 AC Ref 修改为 `AC-05, AC-06`；同步修正自检清单中的 US Ref 声明 | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 在 `followup-rhythm-plan/README.md:验收标准` 中补充"跟进记录归档完成后系统重算下次跟进建议时间"AC；在 `followup-rhythm-plan/README.md:特性概述:范围边界` 外部依赖中声明对 F-02 归档完成事件的触发依赖 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 在 `structured-followup-record/README.md:验收标准` 和 `followup-rhythm-plan/README.md:验收标准` 中分别补充 AC，覆盖"审计日志可按客户 ID、操作人、时间范围检索"场景；确保相关 BR 明确引用 Epic NFR-03 | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-06 | 在 `customer-followup-timeline/README.md:业务规则` BR-02 定义开头添加"参见 Epic [BR-03]"引用 | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-07 | 将 `customer-followup-timeline/README.md:业务对象定义` 中时间线事件的"来源类型"属性统一修改为"创建类型"，并同步更新该文件中 BR 和 AC 的相关属性名称引用 | 产品负责人 | P2 | 待处理 |
| ACT-08 | F-08 | 修订 `customer-followup-timeline/README.md:验收标准` AC-07，使其聚焦"时间线视图不提供删除入口"的 UI 层约束，并注明底层删除保护能力权威来源为 F-02 AC-06，消除与 F-02 AC-06 的冗余表述 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01、F-02、F-03；F-04 标注为待创建，无文档可读取，已在 R1 记录为严重发现）
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
