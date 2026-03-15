---
description: "Epic Review（史诗审核记录）——E-07 数据接入与同步，记录对 E-07 下全部 Feature 定义的系统性审核结论与改进事项"
title: "Epic Review - [E-07] 数据接入与同步 (Data Integration & Sync)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "copilot-product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [E-07] 数据接入与同步 (Data Integration & Sync)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-07] 数据接入与同步（所属 Theme: [T-01] 结构化销售周期）

**Epic 文档路径：** `requirements/structured-sales-cycle/data-integration/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/structured-sales-cycle/data-integration/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/data-integration/f01-channel-config/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md` |
| A0304 需求特性定义 | `requirements/structured-sales-cycle/data-integration/f03-manual-import/README.md` |
| 未创建（F-04） | `requirements/structured-sales-cycle/data-integration/f04-sync-monitor/README.md`（不存在） |
| 未创建（F-05） | `requirements/structured-sales-cycle/data-integration/f05-edm-feedback/README.md`（不存在） |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 2 |
| 一般 | 5 |
| 建议 | 2 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 严重 | `requirements/structured-sales-cycle/data-integration/README.md:功能特性` | Epic 功能特性表中 F-04 同步状态监控（P1）已列入且被业务场景二（手动触发补抓追赶同步、告警清除）显式引用，但对应 A0304 文档 `f04-sync-monitor/README.md` 不存在（标注为"待创建"）。场景二步骤 4-5（管理员手动触发补抓、补抓完成后告警自动清除）及 NFR-03 对"异常补抓须留存日志"的要求，当前均无 Feature 层文档承接，下游 S0306 对该 Feature 无法启动。 | 先执行 S0304，在 `requirements/structured-sales-cycle/data-integration/f04-sync-monitor/` 下新建 `README.md`，覆盖同步状态总览、补抓入口触发、告警推送与清除、操作日志留存的 US/BR/AC。 |
| F-02 | R1 | 严重 | `requirements/structured-sales-cycle/data-integration/README.md:功能特性` | Epic 功能特性表中 F-05 EDM 外发行为回写（P1）已列入且被业务场景四（EDM 互动事件回写至线索行为意向分）显式承接，但对应 A0304 文档 `f05-edm-feedback/README.md` 不存在（标注为"待创建"）。场景四全部步骤（互动事件接收、行为意向分更新、异常降级）当前均无 Feature 层文档承接，下游 S0306 对该 Feature 无法启动。 | 先执行 S0304，在 `requirements/structured-sales-cycle/data-integration/f05-edm-feedback/` 下新建 `README.md`，覆盖 EDM 互动事件逐邮件回传、行为意向分属性更新、异常暂存与补录的 US/BR/AC。 |
| F-03 | R2 | 一般 | `requirements/structured-sales-cycle/data-integration/f01-channel-config/README.md:特性概述:范围边界` | Epic 功能特性表 F-01 范围说明明确约束"V1 中社媒渠道接入数据类型限定为客户互动行为事件，营销绩效数据（曝光量/点击量/阅读量）待 ROI 模块就绪后单独评估接入"，但 F-01 特性概述范围边界仅通过 ASM-03 说明技术可行性待定，完全未承接该 V1 数据类型范围约束。该约束决定了社媒渠道可用时配置端的数据类型选项，属于 F-01 的范围定义，遗漏后下游 S0306 设计渠道类型时将缺乏判断依据。 | 在 `f01-channel-config/README.md` 范围边界中新增条目：V1 阶段即使社媒渠道技术可行性确认，可配置的数据类型亦限于客户互动行为事件；营销绩效数据（曝光量/点击量/阅读量）不在 V1 接入范围内，待 ROI 模块就绪后另行评估（与 Epic 功能特性表.范围说明一致）。 |
| F-04 | R3 | 一般 | `requirements/structured-sales-cycle/data-integration/f01-channel-config/README.md:用户故事` | US-06（修改渠道连接参数或映射规则并留存变更记录）的 AC Ref 仅列 `AC-05`，但 AC-03（配置或修改字段映射规则，验收映射规则保存成功与版本留存）在其 US Ref 中同时引用了 `US-03, US-06`。US-06 对映射规则修改场景未在 AC Ref 中显式引用 AC-03，US→AC 双向追溯断裂，无法从 US-06 直接索引到覆盖其映射规则修改诉求的验收条件。 | 在 `f01-channel-config/README.md` 用户故事表中，将 US-06 的 AC Ref 由 `AC-05` 更新为 `AC-03, AC-05`，恢复双向追溯完整性。 |
| F-05 | R3 | 一般 | `requirements/structured-sales-cycle/data-integration/f03-manual-import/README.md:用户故事` | US-03（在导入时收到与已有线索重复的提示）的 AC Ref 仅列 `AC-03`，但 AC-02（字段映射预览，含"存在潜在重复记录时标注命中行数及匹配依据"）在其 US Ref 中同时引用了 `US-02, US-03`。US-03 对预览阶段重复标注场景未在 AC Ref 中显式引用 AC-02，US→AC 双向追溯断裂：US-03 依赖 AC-02 的预览阶段验收，但两者未正式连接。 | 在 `f03-manual-import/README.md` 用户故事表中，将 US-03 的 AC Ref 由 `AC-03` 更新为 `AC-02, AC-03`，恢复双向追溯完整性。 |
| F-06 | R5 | 一般 | `requirements/structured-sales-cycle/data-integration/f01-channel-config/README.md:业务对象定义` / `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md:业务对象定义` | 渠道配置的接入状态在 F-01 中仅定义"待激活/已激活/已停用"三个值（F-01 BR-02），F-02 将"同步异常"设计为独立的"渠道异常状态"业务对象，而 Epic F-04 范围说明（"提供各渠道同步状态总览：正常/异常/停用"）将接入激活状态与同步健康状态合并为单一视图，三处对渠道状态维度的定义不一致。"停用"出现在两种维度中，"异常"作为同步健康状态未纳入 F-01 的渠道配置状态模型，导致跨 Feature 对渠道状态语义理解存在歧义。 | 在 `f01-channel-config/README.md` 渠道配置业务对象定义中，增加说明"接入状态"仅描述激活维度（待激活/已激活/已停用），同步运行健康状态由 F-02 的渠道异常状态对象独立承载；在 `f02-incremental-sync/README.md` 渠道异常状态对象说明中，明确该对象为独立于接入激活状态的运行健康维度，两者可并存（渠道保持已激活同时处于同步异常）。 |
| F-07 | R7 | 一般 | `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md:业务规则` / `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md:验收标准` | Epic NFR-03 明确"渠道配置变更、手动导入操作、异常补抓须留存完整操作日志，支持按渠道、操作人、时间范围检索"，F-01 BR-06 承接了配置变更日志，F-03 BR-04 承接了导入操作日志，但 F-02 的业务规则章节无对应 BR 承接"异常补抓须留存日志"要求，AC-04 预期结果仅说明"渠道恢复正常同步状态"，未包含补抓操作日志留存的验收项，NFR-03 在 F-02 补抓场景存在承接缺口。 | 在 `f02-incremental-sync/README.md` 业务规则中新增 BR，内容：管理员手动触发的补抓追赶同步操作须写入操作日志，包含触发时间、操作人与补抓执行结果（补抓条数、写入条数、跳过条数），支持按渠道与时间范围检索（参见 Epic [NFR-03]）；并在 AC-04 预期结果中增加"补抓操作日志已留存"的验收项。 |
| F-08 | R4 | 建议 | `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md:业务规则` | F-02 BR-05（有限重试）约定"重试次数须有上限，不得无限重试"，但未给出阈值数值或阈值来源（如"由系统默认配置决定"或"由管理员在渠道配置中设定"）。四要素中判定阈值要素缺失，实现端与验收端均无法明确"上限"为何值，可测试性不足。 | 在 `f02-incremental-sync/README.md` BR-05 中补充阈值来源，例如"重试次数上限由系统默认配置确定"或"不超过 N 次（N 由管理员在渠道配置中设置）"，使阈值有据可查。 |
| F-09 | R6 | 建议 | `requirements/structured-sales-cycle/data-integration/f02-incremental-sync/README.md:验收标准` | F-02 范围边界第 3 条声明"E-01 未就绪时，接入数据需整体暂存，待 E-01 就绪后批量补处理（参见 Epic [DEP-01]）"，但验收标准章节无对应 AC 覆盖此降级场景，该边界条件仅停留在范围声明层面，无法被验收测试验证，存在"声明有但无法验收"的质量风险。 | 在 `f02-incremental-sync/README.md` 验收标准中新增一条 AC，描述前置条件（E-01 不可用）、触发动作（系统到达同步周期并拉取数据）、预期结果（数据进入暂存状态，不执行写入线索池，待 E-01 就绪后触发批量补处理，补处理完成前去重与幂等性要求同样适用）。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 执行 S0304，新建 `requirements/structured-sales-cycle/data-integration/f04-sync-monitor/README.md`，覆盖同步状态总览、补抓入口触发、告警推送与清除、操作日志留存的完整 US/BR/AC | 产品负责人 | P0 | 待处理 |
| ACT-02 | F-02 | 执行 S0304，新建 `requirements/structured-sales-cycle/data-integration/f05-edm-feedback/README.md`，覆盖 EDM 互动事件逐邮件回传、行为意向分属性更新、异常暂存与补录的完整 US/BR/AC | 产品负责人 | P0 | 待处理 |
| ACT-03 | F-03 | 在 `f01-channel-config/README.md` 范围边界中补充 V1 社媒渠道数据类型约束条目（互动行为事件限定，营销绩效数据排除）| 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | 将 `f01-channel-config/README.md` 用户故事表中 US-06 的 AC Ref 由 `AC-05` 更新为 `AC-03, AC-05` | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 将 `f03-manual-import/README.md` 用户故事表中 US-03 的 AC Ref 由 `AC-03` 更新为 `AC-02, AC-03` | 产品负责人 | P1 | 待处理 |
| ACT-06 | F-06 | 在 `f01-channel-config/README.md` 渠道配置业务对象中增加接入激活状态与同步健康状态双维度说明；在 `f02-incremental-sync/README.md` 渠道异常状态对象中明确其为独立于接入激活状态的运行健康维度 | 产品负责人 | P1 | 待处理 |
| ACT-07 | F-07 | 在 `f02-incremental-sync/README.md` 业务规则中新增补抓操作日志留存 BR（承接 Epic [NFR-03]），并在 AC-04 预期结果中增加"补抓操作日志已留存"验收项 | 产品负责人 | P1 | 待处理 |
| ACT-08 | F-08 | 在 `f02-incremental-sync/README.md` BR-05 中补充重试次数上限的阈值来源说明 | 产品负责人 | P2 | 待处理 |
| ACT-09 | F-09 | 在 `f02-incremental-sync/README.md` 验收标准中新增 E-01 不可用降级场景的 AC | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部已存在的 Feature 文档（A0304）全文（F-01、F-02、F-03；F-04、F-05 不存在已在 R1 记录）
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
