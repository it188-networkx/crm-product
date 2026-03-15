---
description: "Epic Review（史诗审核记录）模板，记录对指定需求史诗内全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-02] 知识检索与场景推送 (Knowledge Retrieval)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-17"
last_updated: "2026-03-17"
status: "审核完成"
---

# Epic Review - [E-02] 知识检索与场景推送 (Knowledge Retrieval)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-02] 知识检索与场景推送（所属 Theme: [T-04] 营销知识库）

**Epic 文档路径：** `requirements/knowledge-repository/knowledge-retrieval/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/knowledge-repository/knowledge-retrieval/README.md` |
| A0304 需求特性定义 | `requirements/knowledge-repository/knowledge-retrieval/f01-search/README.md` |
| A0304 需求特性定义 | `requirements/knowledge-repository/knowledge-retrieval/f02-recommendation/README.md` |
| A0304 需求特性定义 | `requirements/knowledge-repository/knowledge-retrieval/f03-feedback/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 3 |
| 建议 | 3 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R3 | 一般 | `f01-search/README.md:用户故事` | Epic 场景一 Step 3"售前顾问浏览检索结果，选择一条竞品应对话术知识单元查看详情（F-01）"在 F-01 用户故事表中无对应 US 覆盖。F-01 特性概述范围边界第 1 条明确列出"知识单元详情查看"属包含范围，但用户故事表中四条 US（US-01～US-04）均聚焦检索列表层操作，无任何 US 描述"选择并查看某条知识单元的完整详情"行为，亦无对应 AC 覆盖该触发动作与预期结果。 | 在 F-01 用户故事中补充 US："作为售前顾问，我想选中检索结果中某条知识单元并查看其完整详情，从而获取完整的案例或话术内容，辅助商机跟进。"同步新增对应 AC，包含前置条件（检索结果已返回且含目标知识单元）、触发动作（选择某条结果查看详情）、预期结果（展示完整知识单元内容，含版本号与发布时间）及 US Ref，修改文件为 `f01-search/README.md` 的用户故事与验收标准章节。 |
| F-02 | R4 | 一般 | `f03-feedback/README.md:业务规则` | F-03 [BR-01]"反馈对象范围"属判定类业务规则，判定依据为"知识单元是否在本次会话中通过 F-01 或 F-02 已展示过"，但"会话"的判定基准（如自登录起至退出或超时前）在文档中未定义；缺少异常数据处理方式（会话状态不可用或会话超时后尝试提交反馈时的系统行为）；判定结果仅说明"不得提交"，未描述结果分流路径（如提示用户"请重新检索或打开推送后再提交"）。四要素不完整，导致该规则无法直接作为测试依据。 | 在 `f03-feedback/README.md` 业务规则章节中完善 [BR-01]：（1）明确"会话"判定基准，例如"自当次登录起至退出或会话超时前"；（2）补充缺失/异常数据处理方式，例如"当会话状态不可用时，不允许提交反馈，系统提示用户重新检索或打开推送列表后再操作"；（3）补充判定结果分流说明：已展示 → 允许提交；未展示 → 拒绝提交并提示。 |
| F-03 | R7 | 一般 | `f01-search/README.md:验收标准`、`f02-recommendation/README.md:验收标准` | Epic NFR-01（知识检索响应 ≤1s，P95，基于关键词+3 维筛选器组合）和 NFR-02（E-01 发布新知识单元后，推荐候选池更新延迟 ≤10 分钟）在 F-01、F-02 的验收标准中均无对应承接 AC，无法通过验收标准验证非功能要求。Epic NFR-03（权限实时过滤，不缓存越权数据）在 F-01 AC-04 和 F-02 中仅通过引用 Epic BR-02 隐式覆盖，无验收标准显式量化确认"实时"与"不缓存"要求。 | （1）在 `f01-search/README.md` 验收标准中新增 NFR-01 对应 AC：前置条件为系统正常运行；触发为发起含关键词与至少 1 个筛选条件的组合检索；预期为 P95 响应时间 ≤1s。（2）在 `f02-recommendation/README.md` 验收标准中新增 NFR-02 对应 AC：前置条件为 E-01 发布新知识单元；触发为等待推荐候选池刷新；预期为该知识单元在 ≤10 分钟内出现在推送候选池（在 E-03 增强接入前适用）。（3）在 F-01/F-02 相关 AC 中显式补充 NFR-03 的"不缓存越权数据"验证场景。 |
| F-04 | R2 | 建议 | `requirements/knowledge-repository/knowledge-retrieval/README.md:功能特性表`、`f03-feedback/README.md:特性概述` | F-03 对 F-01 与 F-02 先行上线的依赖，在 Epic 功能特性表 F-03 行的范围说明中以"需 F-01 上线后方可集成"作非正式注记，但该集成前序依赖未在 Epic 约束与依赖章节以正式 DEP 编号记录；F-03 特性概述范围边界中以"本特性依赖 F-01 与 F-02 的上线，不得早于两者独立集成"自行表述，无法通过"参见 Epic [DEP-xx]"格式追溯至 Epic 层约束，跨 Feature 集成依赖可追溯性不足。 | 在 Epic 约束与依赖章节新增 [DEP-04]（集成前序约束）：说明 F-03 须在 F-01 与 F-02 均已上线后方可集成，影响 F-03。将 `f03-feedback/README.md` 特性概述范围边界第 2 条中的非正式表述替换为"参见 Epic [DEP-04]"格式引用，并保留必要说明文字。Epic 文档修改路径：`requirements/knowledge-repository/knowledge-retrieval/README.md`；Feature 文档修改路径：`f03-feedback/README.md`。 |
| F-05 | R4 | 建议 | `f01-search/README.md:业务规则`、`f02-recommendation/README.md:业务规则` | F-01 的局部 BR 编号 BR-01、BR-02 与同一文档中通过"参见 Epic [BR-01]""参见 Epic [BR-02]"引用的 Epic BR 编号重叠（F-01 业务规则章节同时含 Epic[BR-01]引用与局部[BR-01]"筛选器组合逻辑"定义，Epic[BR-02]引用与局部[BR-02]"结果排序规则"定义）；F-02 存在同等情况（Epic[BR-01/BR-02/BR-03]引用与局部[BR-01/BR-02/BR-03]定义均出现在同一章节）。虽 AC 引用时已一致使用"Epic"/"本地"限定词进行区分，但仅阅读业务规则章节时同名编号易引起混淆，不符合 SSOT 可读性要求。 | 将 F-01 局部 BR 重新编号：BR-01（筛选器组合逻辑）→ BR-S01，BR-02（结果排序规则）→ BR-S02，BR-03（空结果处理）→ BR-S03；将 F-02 局部 BR 重新编号：BR-01（属性匹配策略）→ BR-R01，BR-02（推送触发时机）→ BR-R02，BR-03（空推送处理）→ BR-R03；同步更新对应 AC 中的 BR 引用（移除"本地"限定词，使用新编号直接引用）。修改文件：`f01-search/README.md`、`f02-recommendation/README.md`。 |
| F-06 | R6 | 建议 | `f02-recommendation/README.md:验收标准` | Epic BR-02（权限过滤）要求"客户专属内容仅对相关商机负责人可见"，该约束同时适用 F-01 和 F-02。F-01 已通过 AC-04 专项覆盖检索场景下的权限过滤行为（前置条件：某知识单元为客户专属内容且当前用户非相关商机负责人；预期：该知识单元不出现在检索结果中）。F-02 验收标准中无对等 AC 覆盖推送场景下的同类权限隔离行为；现有 F-02 AC-03 仅覆盖权限过滤后整体无结果的空推送提示场景，未验证单条客户专属知识单元的隐藏行为。 | 在 `f02-recommendation/README.md` 验收标准中新增 AC："前置条件：某知识单元为客户专属内容，当前售前顾问不是相关商机负责人；触发：打开包含该客户对应商机的详情页；预期：该客户专属知识单元不出现在推送列表中（参见 Epic BR-02）；US Ref：US-01"。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 在 `f01-search/README.md` 用户故事章节补充"查看知识单元详情"US，在验收标准章节补充对应 AC（含前置条件、触发动作、预期结果及 US Ref） | 产品负责人（执行 S0304） | P1 | 待处理 |
| ACT-02 | F-02 | 在 `f03-feedback/README.md` 业务规则章节完善 [BR-01]，补充"会话"判定基准定义、会话状态不可用时的异常处理方式及判定结果分流说明 | 产品负责人（执行 S0304） | P1 | 待处理 |
| ACT-03 | F-03 | 在 `f01-search/README.md` 验收标准中补充 NFR-01 对应 AC；在 `f02-recommendation/README.md` 验收标准中补充 NFR-02 对应 AC；在 F-01/F-02 相关 AC 中显式补充 NFR-03 权限实时性验证场景 | 产品负责人（执行 S0304） | P1 | 待处理 |
| ACT-04 | F-04 | 在 `requirements/knowledge-repository/knowledge-retrieval/README.md` 约束与依赖章节新增 [DEP-04] 正式记录 F-03 对 F-01/F-02 的集成前序依赖；在 `f03-feedback/README.md` 特性概述范围边界中以"参见 Epic [DEP-04]"替换当前非正式表述 | 产品负责人（执行 S0303） | P2 | 待处理 |
| ACT-05 | F-05 | 将 `f01-search/README.md` 局部 BR-01～BR-03 重新编号为 BR-S01～BR-S03；将 `f02-recommendation/README.md` 局部 BR-01～BR-03 重新编号为 BR-R01～BR-R03；同步更新两份文档中全部对应 AC 引用 | 产品负责人（执行 S0304） | P2 | 待处理 |
| ACT-06 | F-06 | 在 `f02-recommendation/README.md` 验收标准中新增客户专属知识单元权限过滤的推送场景专项 AC（参见 Epic BR-02，对应 US-01） | 产品负责人（执行 S0304） | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01、F-02、F-03）
- [x] R1 Feature 覆盖完备性检查已执行（Epic 索引 3 个 Feature，3 份文档均存在且各章节非空，无悬空引用）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：业务定义细化展开 ✓；Epic 共享 BR 引用格式 ✓；业务场景步骤对应 US ✓；DEP/ASM 引用承接 ✓，含 F-03 非正式依赖问题已记录为 F-04）
- [x] R3 用户故事完备性检查已执行（步骤覆盖、US-AC 双向追溯逐 Feature 核验；F-01 缺少"查看详情"US 已记录为 F-01）
- [x] R4 BR 引用一致性检查已执行（共享 BR 引用正确性、矛盾检查、四要素检查、编号冲突检查均已核验；F-03 BR-01 四要素问题记录为 F-02，F-01/F-02 编号重叠记录为 F-05）
- [x] R5 业务对象协调性检查已执行（跨 Feature 同名对象职责描述、属性集一致性、状态命名、语义层约束均已核验，无发现）
- [x] R6 验收标准协调性检查已执行（冗余与矛盾检查、Happy Path/异常路径/边界条件覆盖度、AC 引用闭合、三要素完整性均已核验；F-02 权限过滤 AC 缺失记录为 F-06）
- [x] R7 跨 Feature 一致性检查已执行（角色命名、编号唯一性、依赖对称性、范围覆盖、NFR 承接均已核验；NFR 承接缺失记录为 F-03）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论（有条件通过）与问题统计（严重 0、一般 3、建议 3）数据一致
- [x] 改进事项已为每条严重/一般级别的发现（F-01、F-02、F-03）创建对应 Action（ACT-01、ACT-02、ACT-03）
