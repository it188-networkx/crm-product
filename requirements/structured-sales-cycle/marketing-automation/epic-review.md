---
description: "Epic Review（史诗审核记录）——E-05 营销自动化规则管理，对 F-01 规则配置与管理、F-02 规则自动触发执行的系统性审核结论与改进事项"
title: "Epic Review - [E-05] 营销自动化规则管理 (Marketing Automation)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "有条件通过"
---

# Epic Review - [E-05] 营销自动化规则管理 (Marketing Automation)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-05] 营销自动化规则管理（所属 Theme: [T-01] 结构化销售周期）

**Epic 文档路径：** `requirements/structured-sales-cycle/marketing-automation/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/marketing-automation/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/marketing-automation/rule-config/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/marketing-automation/rule-execution/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 6 |
| 建议 | 5 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 一般 | `marketing-automation/README.md:功能特性` | Epic 功能特性表中 [F-03] 规则运行监控（P1）标注"待创建"且对应目录不存在，业务场景三 Step 1（查看规则运行报告）无 A0304 文档承接，构成悬空 Feature 引用。 | 为 F-03 创建 A0304 文档骨架（含范围声明），或在 Epic 功能特性表中为 F-03 明确规划迭代标注，消除悬空引用。 |
| F-02 | R2 | 一般 | `marketing-automation/README.md:业务规则 [BR-01]` / `rule-config/README.md:用户故事` | Epic [BR-01] 要求"标签字典变更时须校验已有规则条件兼容性"。F-01 仅覆盖发布时校验（AC-04），F-02 仅覆盖执行时降级（BR-02），均未通过 US/AC 覆盖"E-06 标签被废弃时主动通知 MKT Leader 更新已激活规则"的场景。 | 在 `rule-config/README.md` 用户故事中补充 US：当已激活规则所用 E-06 标签被废弃时，MKT Leader 收到系统提示并可重新配置规则；并补充对应 AC 验证该通知行为，关联 US-02。 |
| F-03 | R2 | 建议 | `rule-config/README.md:特性概述范围边界` / `rule-execution/README.md:特性概述范围边界` | Epic [ASM-01]（假设：E-06 标签值变更后可在 1 小时内反映到规则触发条件扫描中）在 F-01 和 F-02 的范围边界约束承接列表中均无引用，该上游假设约束信息在 Feature 层丢失。F-02 BR-08 仅覆盖扫描周期时效，未说明标签更新延迟对时间敏感规则准确性的影响。 | 在 `rule-config/README.md` 和 `rule-execution/README.md` 的特性概述范围边界第 3 条（跨 Epic 约束承接）中补充 `参见 Epic [ASM-01]`，确保标签更新延迟风险在 Feature 层可追溯。 |
| F-04 | R3 | 建议 | `rule-execution/README.md:用户故事 US-06` | F-02 US-06 中角色使用"销售"，而 Epic 业务场景二中对应角色为"销售执行层"，两者命名不一致。该角色在 F-02 中仅出现于 US-06 一处，且 AC-05 的预期结果中已隐含销售收到提醒的行为，角色定义不统一影响跨 Feature 一致性。 | 将 `rule-execution/README.md` US-06 中的角色"销售"改为"销售执行层"，与 Epic 业务场景二保持统一。若后续其他 Feature 也涉及同一角色，以"销售执行层"为统一命名。 |
| F-05 | R4 | 建议 | `rule-execution/README.md:业务规则 [BR-03]` | F-02 BR-03（冷却期判定）缺少缺失数据处理方式的明确声明：判定基准为"上一次动作执行完成时间"，但未说明当系统中不存在该客户对该规则的历史执行记录时（如首次触发、系统迁移场景），冷却期判定的处理路径（通常应视为不在冷却期，但未在 BR 中显式声明）。 | 在 `rule-execution/README.md` BR-03 中补充缺失数据处理说明：若该客户对该规则无历史执行记录，则视为不在冷却期，允许本次触发执行。 |
| F-06 | R5 | 建议 | `rule-execution/README.md:业务规则 [BR-05]` / `rule-execution/README.md:业务对象定义 规则触发执行状态` | F-02 BR-05 中使用"待执行状态"描述延迟等待中的执行阶段，而业务对象"规则触发执行状态"的执行状态枚举值定义为"延迟等待中"，两处对同一业务状态使用了不同名称，破坏文档内一致性。 | 将 `rule-execution/README.md` BR-05 中的"系统记录待执行状态"统一改为"系统记录执行状态为'延迟等待中'"，与业务对象定义保持一致。 |
| F-07 | R6 | 一般 | `rule-config/README.md:验收标准` | F-01 BR-03 明确声明"审批拒绝时规则退回草稿状态并保留拒绝原因"，但 F-01 验收标准中无对应 AC 覆盖审批拒绝路径。AC-05 仅覆盖提交审批（状态变为"待审批"），AC-06 仅覆盖审批通过（状态变为"激活"），审批被拒绝后规则状态回退及拒绝原因保留的预期行为缺乏可测试的验收标准。 | 在 `rule-config/README.md` 验收标准中补充 AC：前置条件为规则处于"待审批"状态，触发动作为审批人拒绝审批，预期结果为规则状态退回"草稿"并记录拒绝原因，关联 US-03。 |
| F-08 | R6 | 一般 | `rule-execution/README.md:验收标准` | F-02 BR-07 明确定义"若 E-02 不可用，提醒推送降级为仅发送提醒（不写记录）并在系统层面标记本次执行为'降级执行'"（参见 Epic [DEP-02]），但 F-02 验收标准中无 AC 覆盖该降级执行场景。该场景是 DEP-02 明确建模的依赖降级行为，缺乏 AC 导致该路径在测试中无法被验证。 | 在 `rule-execution/README.md` 验收标准中补充 AC：前置条件为触发条件满足且 E-02 不可用，触发动作为扫描周期到达执行时点，预期结果为系统仅向销售推送提醒通知、不写入 E-02 跟进记录、本次执行被标记为"降级执行"，关联 US-02。 |
| F-09 | R6 | 建议 | `rule-execution/README.md:验收标准` | F-02 BR-02 定义"若触发条件引用的标签在 E-06 中已废弃，该规则本轮扫描跳过该条件匹配，不触发任何动作，并生成异常记录"，但 F-02 验收标准中无 AC 验证该异常处理路径，该行为在测试中无明确验证依据。 | 在 `rule-execution/README.md` 验收标准中补充 AC：前置条件为规则触发条件引用的标签已在 E-06 标签字典中废弃，触发动作为系统执行周期性扫描，预期结果为该规则本轮跳过条件匹配且不触发执行动作，并生成可查询的异常记录。关联 US-01。 |
| F-10 | R7 | 一般 | `marketing-automation/README.md:非功能需求 [NFR-02]` | Epic [NFR-02] 规定"系统须支持同时激活 ≥ 20 条规则，对 ≤ 5000 条活跃客户并发扫描，不影响其他业务操作的响应性能"，但该容量与并发约束在 F-01 和 F-02 的业务规则及验收标准中均无对应承接：F-02 仅承接了 NFR-01（扫描时效 ≤ 1 小时），NFR-02 的性能质量水平无法在 Feature 层被验证。 | 在 `rule-execution/README.md` 业务规则中补充一条引用 Epic [NFR-02] 的 BR，说明扫描执行的容量约束（≥ 20 条激活规则、≤ 5000 活跃客户并发），并在验收标准中补充对应 AC，明确性能边界的验收条件。 |
| F-11 | R7 | 一般 | `marketing-automation/README.md:业务场景三 Step 4` / `rule-execution/README.md:验收标准` | Epic 场景三 Step 4 描述"原触达中的客户按新版本冷却逻辑继续执行"，即新版本规则发布后，处于延迟等待期或冷却期中的客户应按新版本冷却时长重新计算。F-01 AC-08 仅说明"新配置立即对 F-02 扫描生效"，F-02 验收标准中无 AC 明确规定版本切换时，进行中执行流程（延迟等待中状态）和冷却期的重新计算行为，该业务语义存在歧义风险。 | 在 `rule-execution/README.md` 验收标准中补充 AC：前置条件为某客户处于规则延迟等待期或冷却期内，规则新版本（冷却时长变更）发布生效，预期结果明确是"沿用旧版本冷却逻辑直至当前执行周期结束后切换"还是"立即按新版本重新计算"，消除歧义并与 Epic 场景三描述对齐。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 在 `requirements/structured-sales-cycle/marketing-automation/` 下为 F-03 创建 A0304 文档骨架，或在 Epic README 功能特性表中为 F-03 补充规划迭代标注，消除悬空 Feature 引用 | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02 | 在 `rule-config/README.md` 用户故事中补充 US：当 E-06 标签字典中已配置的触发/退出条件标签被废弃时，MKT Leader 收到系统提示；并补充对应 AC 验证该通知与提示行为 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-07 | 在 `rule-config/README.md` 验收标准中补充审批拒绝路径 AC（规则状态退回草稿 + 拒绝原因保留），关联 US-03 | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-08 | 在 `rule-execution/README.md` 验收标准中补充 E-02 不可用时的降级执行 AC（仅推送提醒、不写 E-02 记录、标记"降级执行"），关联 US-02 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-10 | 在 `rule-execution/README.md` 业务规则中补充 NFR-02 容量约束承接（参见 Epic [NFR-02]），并在验收标准中补充对应性能边界 AC | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-11 | 在 `rule-execution/README.md` 验收标准中补充规则版本切换对进行中执行流程（延迟等待期/冷却期）影响的 AC，明确版本切换时的冷却逻辑适用规则，与 Epic 场景三 Step 4 对齐 | 产品负责人 | P1 | 待处理 |
| ACT-07 | F-03 | 在 `rule-config/README.md` 和 `rule-execution/README.md` 特性概述范围边界中补充 `参见 Epic [ASM-01]` 引用，确保标签更新延迟风险可追溯 | 产品负责人 | P2 | 待处理 |
| ACT-08 | F-04 | 将 `rule-execution/README.md` US-06 角色"销售"统一改为"销售执行层"，与 Epic 业务场景二角色命名对齐 | 产品负责人 | P2 | 待处理 |
| ACT-09 | F-05 | 在 `rule-execution/README.md` BR-03 中补充缺失数据处理说明：当该客户对该规则无历史执行记录时，视为不在冷却期，允许本次触发执行 | 产品负责人 | P2 | 待处理 |
| ACT-10 | F-06 | 将 `rule-execution/README.md` BR-05 中"系统记录待执行状态"统一改为"系统记录执行状态为'延迟等待中'"，与业务对象定义的状态枚举值保持一致 | 产品负责人 | P2 | 待处理 |
| ACT-11 | F-09 | 在 `rule-execution/README.md` 验收标准中补充废弃标签扫描跳过路径 AC（跳过匹配、不触发动作、生成异常记录），关联 US-01 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 rule-config/README.md、F-02 rule-execution/README.md；F-03 文档不存在，已在 R1 记录）
- [x] R1 Feature 覆盖完备性检查已执行（双向比对 Epic 索引与实际目录；F-01/F-02 章节完整非空；F-03 悬空引用已记录为 F-01）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：范围说明→业务定义均已细化展开 ✓；BR 引用均含 `参见 Epic [BR-xx]` ✓；场景步骤→US 映射完整 ✓；DEP/ASM 承接中 ASM-01 缺失已记录为 F-03）
- [x] R3 用户故事完备性检查已执行（场景步骤覆盖 ✓；US-AC 双向追溯闭合 ✓；角色命名不一致已记录为 F-04）
- [x] R4 BR 引用一致性检查已执行（共享 BR 引用正确 ✓；无 Feature 覆盖 Epic BR 或矛盾 ✓；BR-03 缺失数据处理已记录为 F-05；BR 局部编号冲突不适用 ✓）
- [x] R5 业务对象协调性检查已执行（跨 Feature 无同名对象冲突 ✓；状态名称 F-01/F-02 一致 ✓；BR 引用属性均在业务对象中存在 ✓；BR-05"待执行状态"命名不一致已记录为 F-06；无实现层信息泄漏 ✓）
- [x] R6 验收标准协调性检查已执行（跨 Feature 无冗余/矛盾 AC ✓；Happy Path 覆盖 ✓；审批拒绝和 E-02 降级异常路径缺失已记录为 F-07/F-08/F-09；AC 三要素完整 ✓；BR 引用编号正确 ✓）
- [x] R7 跨 Feature 一致性检查已执行（角色命名 F-04 已记录 ✓；编号唯一性局部编号符合规则 ✓；依赖对称性 F-01→F-02 引用均有 F-02 范围覆盖 ✓；NFR-01 承接 ✓；NFR-02 缺失已记录为 F-10；版本切换行为覆盖缺口已记录为 F-11）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致（严重 0 → 有条件通过；一般 6；建议 5）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（F-01→ACT-01，F-02→ACT-02，F-07→ACT-03，F-08→ACT-04，F-10→ACT-05，F-11→ACT-06）
