---
description: "Epic Review（史诗审核记录）——[E-06] 客户标签体系管理，审核 F-01/F-02/F-03 三项特性定义的完备性、协调性与一致性"
title: "Epic Review - [E-06] 客户标签体系管理 (Customer Tag Management)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-06] 客户标签体系管理 (Customer Tag Management)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-06] 客户标签体系管理（所属 Theme: [T-01] 结构化销售周期）

**Epic 文档路径：** `requirements/structured-sales-cycle/tag-management/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/tag-management/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/tag-management/tag-dictionary-management/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/tag-management/customer-tagging-conflict/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/tag-management/tag-decay-strategy/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 5 |
| 建议 | 2 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 一般 | `tag-management/README.md:功能特性` | Epic 功能特性表中 [F-04] 标签运营报告（P1）关联文档标注为"待创建"，无对应 A0304 文档，且 Epic 业务场景三步骤 3"MKT Leader 查看衰减规则运行报告、识别衰减率异常客户群"无任何 Feature 文档承接，形成场景覆盖缺口 | 为 [F-04] 执行 S0304 功能特性规划，创建 `tag-management/tag-operation-report/README.md`；或在本轮审核结论中显式标注 F-04 为计划延期项，并在 Epic 功能特性表中补充延期说明，待 F-04 就绪后重新触发 S0309 |
| F-02 | R3 | 一般 | `tag-decay-strategy/README.md:用户故事` | [F-03] US-03（系统定期检查并自动执行标签降级）的 AC Ref 列仅列出"AC-02, AC-03"，但 AC-05（E-02 数据源不可用时规则暂停执行）的 US Ref 指向 US-03；US-03 未将 AC-05 纳入其 AC Ref，导致 US-03 与 AC-05 的双向追溯断裂 | 在 `tag-decay-strategy/README.md:用户故事` 中将 US-03 的 AC Ref 修改为"AC-02, AC-03, AC-05"，使 US→AC 追溯与 AC→US 追溯双向闭合 |
| F-03 | R4 | 建议 | `customer-tagging-conflict/README.md:业务规则` | [F-02] BR-07（手动覆盖权限）是 Epic BR-07（标签字典维护权限）的局部承接，Epic BR-07 同时适用于 F-01（字典维护操作限制）和 F-02（手动打标权限），属于跨 Feature 共享 BR；F-01 BR-06 已正确引用"参见 Epic [BR-07]"，但 F-02 BR-07 未附加"参见 Epic [BR-07]"引用，破坏 SSOT | 在 `customer-tagging-conflict/README.md:业务规则` 中，在 BR-07 末尾追加"（参见 Epic [BR-07]）"，与 F-01 BR-06 的引用方式保持一致 |
| F-04 | R5 | 一般 | `tag-management/README.md:业务场景三` / `customer-tagging-conflict/README.md:业务对象定义` / `tag-decay-strategy/README.md:业务对象定义` | Epic 业务场景三步骤 2 明确"标签衰减操作记录至客户标签变更日志（时间、规则触发条件、原值与新值）"；然而 F-02"标签变更日志"的操作类型枚举（自动打标/AI 建议确认/AI 建议拒绝/手动覆盖/冲突解决/手动重置）未包含"衰减"类型；F-03 另行定义了独立的"衰减执行记录"对象，且未声明其与 F-02"标签变更日志"的关系，导致衰减操作的日志归属存在歧义：衰减日志究竟写入统一的"标签变更日志"还是独立的"衰减执行记录" | 明确业务设计决策：若衰减操作日志写入统一"标签变更日志"，则在 F-02 `customer-tagging-conflict/README.md:业务对象定义` 的标签变更日志操作类型中增加"衰减操作"枚举值，并在 F-03 `tag-decay-strategy/README.md:业务对象定义` 中说明"衰减执行记录"是"标签变更日志"的衰减类型子集；若设计为两套独立日志，则在 Epic 业务场景三步骤 2 中将"客户标签变更日志"修正为"衰减执行记录"，并在 F-02 范围边界中明确声明"不包含衰减操作日志" |
| F-05 | R6 | 一般 | `tag-dictionary-management/README.md:验收标准` | [F-01] 验收标准缺少两类边界/异常路径 AC：(1) BR-01 违反场景——创建或修改标签时名称在全库已存在，无 AC 定义系统应如何响应；(2) BR-04 违反场景——提交人尝试对自己提交的变更执行审批通过操作，虽然 AC-01 的触发动作中隐含"不同账号"，但无独立 AC 明确系统应阻止自审批并给出错误提示 | 在 `tag-dictionary-management/README.md:验收标准` 中补充：(1) 一条命名冲突异常路径 AC：前置条件为目标名称在全库已存在，触发动作为提交创建/修改，预期结果为系统拒绝并提示具体冲突来源（参见 BR-01）；(2) 一条自审批阻断 AC：前置条件为提交人与当前审批操作人为同一账号，触发动作为提交方发起审批通过操作，预期结果为系统阻止操作并提示不可自审批（参见 BR-04） |
| F-06 | R7 | 一般 | `customer-tagging-conflict/README.md:用户故事` | [F-02] 用户故事（US-02、US-03、US-05）统一使用"销售"作为角色名称，而 Epic 业务场景二定义的角色为"销售执行层"，且 F-02 自身 AC-04 前置条件中也使用"销售执行层"；同一角色在同一 Feature 内部（US 与 AC 之间）及跨特性与 Epic 之间存在命名不一致，违反 R7 角色命名统一要求 | 在 `customer-tagging-conflict/README.md:用户故事` 中，将 US-02、US-03、US-05 的角色列从"销售"统一修改为"销售执行层"，与 Epic 业务场景及 F-02 自身 AC-04 的命名对齐 |
| F-07 | R7 | 建议 | `tag-management/README.md:非功能需求` / 三份 A0304 验收标准 | Epic NFR-01（标签查询响应时间不超过 500 毫秒）和 NFR-02（系统支持 ≥ 100 个活跃标签条目，单客户 ≥ 20 个有效标签）在 F-01、F-02、F-03 的验收标准中均无对应承接 AC，下游 S0306 设计与测试阶段无法从 Feature 层获得可验证的性能与容量质量门禁 | 在最直接承接上述 NFR 的 Feature 验收标准中各补充一条非功能 AC：在 `tag-dictionary-management/README.md` 或 `customer-tagging-conflict/README.md` 中为 NFR-01 补充响应时间 AC（前置条件：标签字典已发布，触发动作：触发标签查询，预期结果：响应时间 ≤ 500ms）；在 `tag-dictionary-management/README.md` 中为 NFR-02 补充容量边界 AC（前置条件：活跃标签条目数达 100，单客户关联 20 个标签，触发动作：创建第 101 个/第 21 个，预期结果：系统正常处理而非降级失败） |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 为 [F-04] 标签运营报告执行 S0304 创建 `tag-management/tag-operation-report/README.md`；或在 Epic 功能特性表中为 F-04 补充延期说明，明确下游 S0306 范围不含 F-04，待 F-04 就绪后重新审核 | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02 | 将 `tag-decay-strategy/README.md:用户故事` 中 US-03 的 AC Ref 修改为"AC-02, AC-03, AC-05"，修复 US-03 与 AC-05 的双向追溯断裂 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-04 | 在 Epic 业务场景三步骤 2 和 F-02/F-03 业务对象定义中澄清衰减日志的归属设计：统一写入 F-02 标签变更日志（并补充"衰减操作"枚举值），或明确为独立的 F-03 衰减执行记录（并修正 Epic 描述与 F-02 范围声明） | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-05 | 在 `tag-dictionary-management/README.md:验收标准` 中补充命名冲突异常路径 AC 和自审批阻断边界条件 AC，覆盖 BR-01 与 BR-04 的约束验证场景 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-06 | 将 `customer-tagging-conflict/README.md:用户故事` 中 US-02、US-03、US-05 的角色名称从"销售"统一修改为"销售执行层"，消除跨 Feature 及 Feature 内部的角色命名不一致 | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-03 | 在 `customer-tagging-conflict/README.md:业务规则` 中为 BR-07 末尾追加"（参见 Epic [BR-07]）"引用，与 F-01 BR-06 的引用方式保持一致 | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-07 | 在相关 Feature 的验收标准中为 Epic NFR-01（查询响应 ≤ 500ms）和 NFR-02（容量边界）各补充一条可验证的非功能 AC，形成下游 S0306 设计与测试的质量门禁 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 tag-dictionary-management、F-02 customer-tagging-conflict、F-03 tag-decay-strategy；F-04 无文档，已在 R1 中记录）
- [x] R1 Feature 覆盖完备性检查已执行
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：业务定义细化展开均已达标；BR 引用整体正确，F-02 BR-07 缺少 Epic 引用已记录；场景步骤到用户故事覆盖整体达标；DEP/ASM 在 Feature 层均已承接，ASM-01 未被 Feature 显式引用但属外部前提假设，不影响通过）
- [x] R3 用户故事完备性检查已执行（步骤覆盖、US-AC 双向追溯；F-03 US-03 双向断裂已记录）
- [x] R4 BR 引用一致性检查已执行（引用正确性、矛盾检查、四要素检查；F-02 BR-07 缺少 Epic 引用已记录；BR 编号各 Feature 为局部编号，跨 Feature 无引用冲突）
- [x] R5 业务对象协调性检查已执行（命名、属性、状态、语义层；衰减日志归属歧义已记录）
- [x] R6 验收标准协调性检查已执行（冗余、矛盾、覆盖度、引用闭合；F-01 缺少两类异常路径 AC 已记录）
- [x] R7 跨 Feature 一致性检查已执行（角色、编号、依赖、范围、NFR；F-02 角色命名不一致和 NFR-01/NFR-02 无 AC 承接均已记录）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致（严重 0、一般 5、建议 2 → 有条件通过）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（ACT-01～ACT-05 对应 F-01～F-06；ACT-06～ACT-07 对应建议级发现）
