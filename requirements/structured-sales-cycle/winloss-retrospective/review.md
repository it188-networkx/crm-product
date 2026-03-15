---
description: "Epic Review（史诗审核记录）——[E-04] 成交复盘与策略回流，记录对 Epic 及其全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-04] 成交复盘与策略回流 (Win/Loss Retrospective)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-04] 成交复盘与策略回流 (Win/Loss Retrospective)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-04] 成交复盘与策略回流（所属 Theme: structured-sales-cycle）

**Epic 文档路径：** `requirements/structured-sales-cycle/winloss-retrospective/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/winloss-retrospective/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/winloss-retrospective/structured-review/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/winloss-retrospective/ai-consistency-check/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/winloss-retrospective/strategy-backflow/README.md` |

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
| F-01 | R3 | 一般 | `winloss-retrospective/structured-review/README.md:用户故事` | Epic 业务场景三 Step 3 明确描述"管理员可将优质成交复盘标记为'经验参考'，供销售团队在同类商机推进时参阅"，但 [F-01] 结构化复盘录入的用户故事表中无任何 US 覆盖该步骤，"管理员"角色未在 F-01 的业务规则或验收标准中承接。该步骤是 Epic 明确声明的业务场景步骤，在 Feature 层完全缺席。 | 在 `structured-review/README.md:用户故事` 中新增 US（As a 管理员，I want to 将优质成交复盘标记为经验参考，So that 销售团队可在同类商机推进时参阅），并在 `业务规则` 中补充对应 BR（明确标记权限与标记/取消标记条件），在 `验收标准` 中补充 AC 覆盖标记成功路径与权限校验路径。 |
| F-02 | R6 | 一般 | `winloss-retrospective/strategy-backflow/README.md:验收标准` | Epic 业务场景二 Step 3 声明三种操作路径（采纳、修改、拒绝），[F-03] 策略回流审核的 US-02 和 US-04 亦均声明"逐条进行采纳、修改或拒绝"，业务对象"策略回流建议"也定义了"已修改"业务状态。然而 F-03 验收标准中无任何 AC 覆盖"修改"路径（AC-02 仅覆盖采纳路径，AC-03 仅覆盖拒绝路径），导致"已修改"状态在验收标准层不可验证，该操作路径缺乏可测试的验收定义。 | 在 `strategy-backflow/README.md:验收标准` 中补充"修改"路径 AC：前置条件——负责人查看待审核建议；触发动作——负责人修改建议内容并确认提交；预期结果——建议状态变为"已修改"，修改说明与审批人、审批时间记录留存（参见 BR-04），触发对应下游审批流（参见 BR-03），并关联至 US-02 / US-04。 |
| F-03 | R7 | 严重 | `winloss-retrospective/ai-consistency-check/README.md:业务规则 / 验收标准` | Epic NFR-02 明确要求"复盘内容（含竞品分析、客户决策信息）不得明文传输至外部 AI 服务，须进行脱敏预处理（承接 GC-03）"。[F-02] AI 一致性比对是整个 Epic 中唯一调用外部 AI 服务的 Feature，是 NFR-02 的直接承接方。但 F-02 全部 6 条业务规则（BR-01 至 BR-06）和全部 6 条验收标准（AC-01 至 AC-06）均无任何承接，既无要求脱敏预处理的 BR，也无验证脱敏行为的 AC，导致该安全合规要求在 Feature 层完全断链。下游 S0306 功能特性设计将因此缺乏来自 F-02 的脱敏设计指令，存在安全合规风险。 | 在 `ai-consistency-check/README.md:业务规则` 中新增 BR，明确"调用 AI 比对服务前须对复盘数据进行脱敏预处理（承接 Epic NFR-02、GC-03）"，脱敏范围须包含失单原因、竞争对手、客户决策信息等敏感字段；在 `验收标准` 中补充 AC，验证 AI 比对前数据脱敏处理行为（可作为 AC-01 的前置条件扩充），覆盖正常脱敏路径与脱敏服务异常降级路径。 |
| F-04 | R7 | 一般 | `winloss-retrospective/structured-review/README.md:业务规则` / `winloss-retrospective/ai-consistency-check/README.md:业务规则` | Epic NFR-03 明确要求"复盘录入、修正，AI 比对结果裁定，回流建议审批等操作须留存完整审计日志（承接 GC-04）"，该 NFR 覆盖了 [F-01]（复盘录入/修正操作）和 [F-02]（AI 比对裁定操作）。然而 F-01 业务规则（BR-01 至 BR-05）和验收标准中均无承接，F-02 业务规则（BR-01 至 BR-06）和验收标准中亦无承接。[F-03] 通过继承 Epic BR-06 间接覆盖了回流建议审批的审计要求，F-01 与 F-02 构成合规要求断链。 | 在 `structured-review/README.md:业务规则` 中新增 BR，引用 Epic NFR-03，明确"复盘录入与修正操作须留存完整审计日志（承接 Epic NFR-03、GC-04）"；在 `ai-consistency-check/README.md:业务规则` 中同样新增 BR，明确"AI 比对结果裁定操作须留存完整审计日志（承接 Epic NFR-03、GC-04）"；两处同步在验收标准中补充相应 AC。 |
| F-05 | R7 | 一般 | `winloss-retrospective/README.md:业务场景三 Step 3` 及 `structured-review/README.md:特性概述:范围边界` | Epic 业务场景三 Step 3 声明"管理员可将优质成交复盘标记为'经验参考'"，该业务能力在全部三个 Feature（F-01/F-02/F-03）的范围边界"包含"列表中均未出现，Epic 功能特性表中 F-01 的范围说明"成交场景为建议性录入，覆盖关键成功因素、决策触发要素、竞争优势点"亦未涵盖此能力，形成 Epic 业务场景声明与 Feature 联合覆盖范围之间的完整缺口。该发现与 F-01（R3）从范围维度提供独立记录。 | 在 Epic `README.md:功能特性表` F-01 的范围说明中补充"管理员标记优质成交复盘为经验参考"能力，并在 `structured-review/README.md:特性概述:范围边界`"包含"列表中相应增加该能力描述，使 Feature 范围覆盖与 Epic 业务场景保持一致。 |
| F-06 | R4 | 建议 | `winloss-retrospective/structured-review/README.md:业务规则 BR-01` / `winloss-retrospective/ai-consistency-check/README.md:业务规则 BR-02 BR-03` / `winloss-retrospective/strategy-backflow/README.md:业务规则 BR-02 BR-04` | 多处 Feature BR 大量复制了 Epic BR 的正文内容后在括注中标记"继承 Epic BR-xx"，而非遵循"以 `参见 Epic [BR-xx]` 引用、仅保留 Feature 增量约束"的 SSOT 原则。具体例证：F-01 BR-01 大量复制 Epic BR-01 正文；F-02 BR-02 近乎原文复制 Epic BR-03；F-02 BR-03 大量复制 Epic BR-04；F-03 BR-02 大量复制 Epic BR-05；F-03 BR-04 大量复制 Epic BR-06。若 Epic BR 将来修订，各 Feature 中的重复正文将与 Epic 产生不一致，造成维护风险。 | 将各 Feature BR 中与 Epic BR 内容重复的正文简化为"参见 Epic [BR-xx]"，其后仅保留该 Feature 特有的增量约束内容；如无增量约束，BR 正文仅保留引用语句。 |
| F-07 | R6 | 建议 | `winloss-retrospective/ai-consistency-check/README.md:验收标准` | [F-02] BR-05 明确规定"异常标记复盘须由对应销售人员在规定时限内（默认 48 小时）完成二次确认"，但 F-02 全部 6 条验收标准（AC-01 至 AC-06）中无 AC 覆盖"二次确认时限到期仍未裁定"的超时场景，系统在超时后的具体行为（是否发送提醒、是否标记为逾期裁定等）缺乏可验收定义，该边界条件缺失。 | 在 `ai-consistency-check/README.md:验收标准` 中补充超时边界 AC：前置条件——复盘被标记为异常且二次确认时限到期；触发动作——时限到期事件；预期结果——系统执行 BR-05 定义的行为（需 BR-05 先补充超时处理规则，建议与 F-01 的 BR-01 逾期处理机制保持一致）。 |
| F-08 | R5 | 建议 | `winloss-retrospective/strategy-backflow/README.md:业务规则 BR-01` / `winloss-retrospective/structured-review/README.md:业务对象定义:复盘记录` | [F-03] BR-01 将回流建议的归纳基准表述为"同类失单原因达到归纳阈值"，但该术语与 [F-01] 复盘记录业务对象中正式定义的属性名称"失单原因一级分类"不一致。两个 Feature 对同一业务概念使用不同术语，导致 F-03 建议归纳逻辑的语义基础无法追溯到 F-01 业务对象定义中的具体属性，跨 Feature 术语不统一。 | 在 `strategy-backflow/README.md:业务规则 BR-01` 中将"同类失单原因"替换为"失单原因一级分类"（直接引用 F-01 复盘记录中已定义的属性名称），使 F-03 的归纳逻辑可从 F-01 业务对象定义追溯到具体属性，保持跨 Feature 业务术语一致性。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-03 | 在 `ai-consistency-check/README.md:业务规则` 中新增数据脱敏 BR（承接 Epic NFR-02、GC-03），明确调用 AI 服务前须对复盘数据进行脱敏预处理，覆盖脱敏范围；在 `验收标准` 中补充脱敏处理 AC，覆盖正常路径与脱敏异常降级路径。 | 产品负责人 | P0 | 待处理 |
| ACT-02 | F-01, F-05 | 在 Epic `README.md:功能特性表` 中更新 F-01 范围说明，补充"管理员标记优质成交复盘为经验参考"能力；在 `structured-review/README.md:用户故事` 中新增对应 US，在 `业务规则` 中补充权限与条件 BR，在 `验收标准` 中补充对应 AC；同步在 `特性概述:范围边界` 中将该能力列为"包含"。 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-02 | 在 `strategy-backflow/README.md:验收标准` 中补充"修改建议内容"路径 AC，覆盖触发动作、已修改状态变更、审批记录留存、下游审批流触发；关联至 US-02 / US-04。 | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 在 `structured-review/README.md:业务规则` 中新增引用 Epic NFR-03 的审计日志 BR，并补充对应 AC；在 `ai-consistency-check/README.md:业务规则` 中新增引用 Epic NFR-03 的审计日志 BR，并补充对应 AC。 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-06 | 将 `structured-review/README.md:BR-01`、`ai-consistency-check/README.md:BR-02 BR-03`、`strategy-backflow/README.md:BR-02 BR-04` 中重复 Epic BR 正文内容的部分简化为"参见 Epic [BR-xx]"加增量约束的格式，消除双重定义。 | 产品负责人 | P2 | 待处理 |
| ACT-06 | F-07 | 在 `ai-consistency-check/README.md:业务规则 BR-05` 中补充二次确认超时的处理规则（参照 BR-01 逾期提醒机制），并在 `验收标准` 中补充对应超时边界 AC。 | 产品负责人 | P2 | 待处理 |
| ACT-07 | F-08 | 在 `strategy-backflow/README.md:业务规则 BR-01` 中将"同类失单原因"替换为"失单原因一级分类"，与 F-01 复盘记录属性名称对齐。 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 结构化复盘录入、F-02 AI 一致性比对、F-03 策略回流审核）
- [x] R1 Feature 覆盖完备性检查已执行（三个 Feature 文档均存在且 US/BR/AC 章节非空，双向索引闭合）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：范围说明->业务定义细化展开通过；Epic BR 继承引用通过；Epic 场景步骤->US 覆盖发现 F-01 缺口；DEP/ASM 承接位于范围边界而非业务规则，记录为建议）
- [x] R3 用户故事完备性检查已执行（步骤覆盖发现 F-01 管理员角色缺失；US-AC 双向引用检查通过；角色一致性检查通过）
- [x] R4 BR 引用一致性检查已执行（引用正确性通过；四要素检查通过；Feature BR 重复 Epic BR 内容记录为建议；局部编号无跨 Feature 引用冲突）
- [x] R5 业务对象协调性检查已执行（复盘记录跨 Feature 属性集无矛盾；状态名称一致；F-03 术语与 F-01 属性名称不一致记录为建议；无实现细节泄漏）
- [x] R6 验收标准协调性检查已执行（跨 Feature 无冗余或矛盾 AC；F-03 修改路径 AC 缺失记录为一般；F-02 超时边界 AC 缺失记录为建议；AC 三要素完整性通过）
- [x] R7 跨 Feature 一致性检查已执行（角色命名统一；编号无跨 Feature 引用冲突；依赖对称性通过；Epic 场景三管理员范围缺口记录为一般；NFR-02 安全承接断链记录为严重；NFR-03 部分承接断链记录为一般）
- [x] 每条发现均引用具体文件路径与章节位置
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致（严重 1 条 -> 不通过）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（F-01 至 F-05 对应 ACT-01 至 ACT-04，合并同根同类）
