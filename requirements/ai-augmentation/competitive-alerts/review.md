---
description: "Epic Review（史诗审核记录），记录对 T-02/E-03 竞品预警与监控 Epic 内全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [T-02/E-03] 竞品预警与监控 (Competitive Alerts & Monitoring)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [T-02/E-03] 竞品预警与监控 (Competitive Alerts & Monitoring)

## 审核摘要 (Review Summary)

**审核范围：** Epic [T-02/E-03] 竞品预警与监控（所属 Theme: [T-02] AI 增强与竞品智能）

**Epic 文档路径：** `requirements/ai-augmentation/competitive-alerts/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/ai-augmentation/competitive-alerts/README.md` |
| A0304 需求特性定义 | `requirements/ai-augmentation/competitive-alerts/competitive-alert-push/README.md` |

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
| F-01 | R2 | 一般 | `competitive-alert-push/README.md:业务规则:BR-08` | Feature BR-08「定版备注」覆盖了 Epic BR-07「备注关联」的全部业务内容，但未通过 `参见 Epic [BR-07]` 建立引用关系，违反 SSOT 原则；更关键的是，Epic BR-07 明确约束备注信息须"供 E-02 跟进辅助在引用应对上下文时参考"（跨 Epic 数据消费依赖），该约束在 Feature BR-08 中被完全丢弃，造成下游 S0306 功能特性设计阶段无法感知此跨 Epic 依赖 | 在 Feature BR-08 末尾补充 `（参见 Epic [BR-07]）`；同时还原 E-02 上下文注入的说明：备注内容须能被 E-02 跟进辅助消费，与 Epic DEP-04 数据结构共享要求保持一致 |
| F-02 | R3 | 一般 | `requirements/ai-augmentation/competitive-alerts/README.md:业务场景:场景二:步骤3` vs `competitive-alert-push/README.md:用户故事` | Epic 业务场景二第 3 步明确要求"更新后的预警通知相关方（F-01）"，即风险等级调整确认后须同步通知 MKT Leader 与责任销售。Feature 用户故事与验收标准中无任何 US 或 AC 覆盖此通知行为；US-05 仅覆盖售前确认调整，AC-08 仅要求留存变更记录，均不涉及通知 MKT / 责任销售 | 在 `competitive-alert-push/README.md:用户故事` 中新增 US（分别对应 MKT Leader 和责任销售的通知接收场景），并在验收标准中新增对应 AC，明确前置条件（已定版预警风险等级调整确认生效）、触发动作与预期结果（MKT Leader 与责任销售收到等级变更通知） |
| F-03 | R5 | 一般 | `competitive-alert-push/README.md:业务规则:BR-11` vs `competitive-alert-push/README.md:业务对象定义:竞品预警记录` | BR-11 的触发判定依赖两个时间戳："自上次信息更新起超过 2 周（14 自然日）"与"自定版或上次等级调整起超过 4 周（28 自然日）未降级"，但竞品预警记录业务对象定义中不存在"信息最后更新时间"或"上次等级调整时间"属性；下游 S0306 设计阶段将无法为 AI 提醒逻辑找到数据载体 | 在 `competitive-alert-push/README.md:业务对象定义:竞品预警记录` 中新增两个业务属性：（1）"信息最后更新时间"——标识本条预警最近一次关联情报信息补充的时间点；（2）"等级最后调整时间"——标识本条预警最近一次风险等级确认或调整的时间点（定版时初始化为定版时间） |
| F-04 | R5 | 一般 | `competitive-alert-push/README.md:业务规则:BR-10` vs `competitive-alert-push/README.md:业务对象定义:竞品预警记录` | BR-10 要求"每次调整须留存变更前后等级、触发信息与确认人记录"，但竞品预警记录业务对象定义中无对应属性承载等级变更历史；风险等级仅定义为当前快照值（"风险等级"单值属性），无法支撑 BR-10 要求的变更追溯与 NFR-03 的操作审计 | 在 `competitive-alert-push/README.md:业务对象定义:竞品预警记录` 中新增"风险等级调整记录"属性（描述：本条预警历次风险等级变更的有序记录，每条包含变更前等级、变更后等级、触发信息摘要与确认售前）；或将等级调整历史提升为独立业务对象，并在预警记录中以关联关系引用 |
| F-05 | R6 | 一般 | `competitive-alert-push/README.md:验收标准:AC-08` | AC-08 仅验证"AI 推荐到售前确认"主流程及变更记录留存，未覆盖风险等级调整确认后通知相关方的验收场景；Epic 场景二步骤 3 要求调整确认后"通知相关方"，但 AC-08 的预期结果中无此要求，致使该通知行为进入 S0306 设计阶段时缺乏可测验收基准 | 在 AC-08 的预期结果中增加通知验收条件：风险等级调整确认生效后，MKT Leader 与受影响客户的责任销售收到等级变更通知（E-01 不可用时降级为仅通知 MKT Leader）；或在 F-02 改进中通过新增 AC 独立覆盖此场景 |
| F-06 | R7 | 一般 | `requirements/ai-augmentation/competitive-alerts/README.md:非功能需求` vs `competitive-alert-push/README.md:验收标准` | Epic NFR-01（竞品情报提交到售前定版触发通知，端到端时延 ≤ 24 小时）和 NFR-02（新增关联信息后 AI 完成风险等级重新评估并推荐调整，时延 ≤ 1 小时）在 Feature 的业务规则与验收标准中均无承接；Feature AC 中仅对业务流程做功能性验收，未对上述时效 SLA 设置任何验收条件，下游 S0306 无依据纳入时效约束设计 | 在 `competitive-alert-push/README.md:验收标准` 中新增两条 AC 分别承接 NFR-01 和 NFR-02：（1）AC-NFR-01：情报提交完成后，售前完成定版并触发通知的端到端时延不超过 24 小时（注明标记"[推导-待确认]"）；（2）AC-NFR-02：已定版预警新增关联情报后，AI 完成风险等级重新评估并向售前输出推荐方案的时延不超过 1 小时（注明标记"[推导-待确认]"） |
| F-07 | R2 | 建议 | `competitive-alert-push/README.md:特性概述:范围边界` | Epic ASM-01（竞品信息时效假设：外部数据来源更新频率不足时 NFR-01 时效性可能无法满足，影响 F-01）在 Feature 范围边界与业务规则中均未被引用；Epic DEP-01~DEP-04 已在范围边界第 3-6 条以 `参见 Epic [DEP-xx]` 形式承接，但 ASM-01 被遗漏，造成时效性假设风险在 Feature 层不可见 | 在 `competitive-alert-push/README.md:特性概述:范围边界` 的外部依赖说明中（第 3 条或单独第 7 条）增加对 ASM-01 的引用：外部数据来源更新频率不足时，预警时效性 NFR-01 可能无法满足，参见 Epic [ASM-01] |
| F-08 | R6 | 建议 | `competitive-alert-push/README.md:验收标准` vs `competitive-alert-push/README.md:业务规则:BR-09` | BR-09 明确规定"若提取结果未识别出竞品名称或受影响客户，须提示提交人手动补全，确认后的情报记录须至少包含竞品名称、威胁描述与受影响客户（≥1 名），否则不可录入"，但验收标准中无对应 AC 验证此异常路径；AC-01 仅通过 `参见 BR-09` 做了形式引用，实际预期结果描述的是成功录入路径，未覆盖 AI 提取失败后的提示与强制补全行为 | 在验收标准中补充 AC：前置条件为 AI 关键词提取结果缺失竞品名称或受影响客户；触发动作为提交人提交；预期结果为系统展示补全提示，要求提交人手动填写缺失字段，未完成补全时不可录入（参见 BR-09） |
| F-09 | R7 | 建议 | `requirements/ai-augmentation/competitive-alerts/README.md:业务场景:场景一` vs `competitive-alert-push/README.md:用户故事` | Epic 业务场景"用户"栏使用"售前执行层"与"销售执行层"角色标签，而场景步骤正文及 Feature 用户故事统一使用"售前"与"责任销售"；Epic 概述与功能特性表也使用"MKT、售前与责任销售"；两套命名并存于同一 Epic 文档，使读者无法确认"售前执行层"是否等同于"售前"、"销售执行层"是否等同于"责任销售" | 在 Epic 文档 `requirements/ai-augmentation/competitive-alerts/README.md:业务场景` 的场景"用户"栏中，将"售前执行层"与"销售执行层"统一修订为"售前"与"责任销售"，与场景步骤正文、功能特性表和 Feature 文档保持一致 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 在 `competitive-alert-push/README.md:业务规则:BR-08` 末尾补充 `（参见 Epic [BR-07]）`，并还原 E-02 上下文注入约束（备注内容须能被 E-02 跟进辅助消费） | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02, F-05 | 在 `competitive-alert-push/README.md:用户故事` 中新增风险等级调整后通知相关方的 US（MKT Leader 侧和责任销售侧各一条），并在验收标准中新增对应 AC，覆盖 AC-08 中缺失的通知验收条件 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-03 | 在 `competitive-alert-push/README.md:业务对象定义:竞品预警记录` 中新增"信息最后更新时间"与"等级最后调整时间"两个业务属性 | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 在 `competitive-alert-push/README.md:业务对象定义:竞品预警记录` 中新增"风险等级调整记录"属性，描述历次等级变更记录（变更前等级、变更后等级、触发信息摘要、确认售前） | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-06 | 在 `competitive-alert-push/README.md:验收标准` 中新增 AC 承接 Epic NFR-01（定版通知端到端时延 ≤ 24 小时）和 NFR-02（AI 风险等级重评推荐时延 ≤ 1 小时），均保留 `[推导-待确认]` 标注 | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-07 | 在 `competitive-alert-push/README.md:特性概述:范围边界` 中补充 ASM-01 引用，说明外部来源时效性假设对 NFR-01 的潜在影响 | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-08 | 在 `competitive-alert-push/README.md:验收标准` 中新增 AI 提取失败场景的 AC，验证系统在缺失竞品名称或受影响客户时的提示与强制补全行为 | 产品负责人 | P2 | 待处理 |
| ACT-08 | F-09 | 将 `requirements/ai-augmentation/competitive-alerts/README.md:业务场景` 中各场景"用户"栏的"售前执行层"统一修订为"售前"、"销售执行层"统一修订为"责任销售" | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文
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
