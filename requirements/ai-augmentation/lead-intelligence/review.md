---
description: "Epic Review（史诗审核记录），记录对 E-01「AI 线索智能研判」Epic 及其全部下属 Feature 定义的系统性审核结论与改进事项"
title: "Epic Review - [T-02/E-01] AI 线索智能研判 (AI Lead Intelligence)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
task_id: "101508"
sprint: "20260309"
---

# Epic Review - [T-02/E-01] AI 线索智能研判 (AI Lead Intelligence)

## 审核摘要 (Review Summary)

**审核范围：** Epic [T-02/E-01] AI 线索智能研判（所属 Theme: [T-02] AI 辅助增强，路径: `requirements/ai-augmentation/lead-intelligence/`）

**Epic 文档路径：** `requirements/ai-augmentation/lead-intelligence/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/ai-augmentation/lead-intelligence/README.md` |
| A0304 需求特性定义（F-01） | `requirements/ai-augmentation/lead-intelligence/lead-scoring/README.md` |
| A0304 需求特性定义（F-02） | `requirements/ai-augmentation/lead-intelligence/anomaly-detection/README.md` |
| A0304 需求特性定义（F-03） | `requirements/ai-augmentation/lead-intelligence/assignment-recommendation/README.md` |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 1 |
| 一般 | 4 |
| 建议 | 2 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R2 | 一般 | `lead-scoring/README.md:业务规则`、`anomaly-detection/README.md:业务规则`、`assignment-recommendation/README.md:业务规则` | Epic [ASM-01]（用户授权管理）标注适用 F-01、F-02、F-03，但三个 Feature 的业务规则章节均未通过 `参见 Epic [ASM-01]` 承接该约束。F-01 虽以 BR-06（重评资格限制）落地了授权约束的业务行为，但未显式引用 ASM-01 来源，导致从 Feature 层无法回溯该约束的上游依据；F-02 和 F-03 亦未在业务规则中对 ASM-01 进行任何形式的承接或引用，违反向下拆分契约第 (4) 条映射（DEP/ASM 应在 Feature 业务规则中以引用方式承接）。 | 在 F-01 `lead-scoring/README.md:业务规则` 中补充一条 BR 引用 `参见 Epic [ASM-01]`，描述授权体系不可用时功能不可操作的降级行为；在 F-02 `anomaly-detection/README.md:业务规则` 和 F-03 `assignment-recommendation/README.md:业务规则` 中同样补充对应的 `参见 Epic [ASM-01]` 引用 BR，明确各 Feature 依赖授权机制区分 MKT Leader 与销售执行层操作权限的前提。 |
| F-02 | R4 | 一般 | `assignment-recommendation/README.md:业务规则` | Epic [BR-01]（评分全覆盖）明确标注适用 F-01 和 F-03，属于跨两个 Feature 的共享 BR。F-01 已在其业务规则第一条以 `参见 Epic [BR-01]` 正确引用。F-03 的业务规则章节（BR-01 至 BR-06）未包含任何对 Epic [BR-01] 的引用，违反 R4 共享 BR 必须在各适用 Feature 中通过 `参见 Epic [BR-xx]` 正确引用的要求。F-03 分配推荐依赖授权用户可见且可查的评分结果与分级建议，该可见性约束来源于 Epic BR-01，缺少引用导致该约束在 F-03 层无法追溯。 | 在 F-03 `assignment-recommendation/README.md:业务规则` 中新增一条 BR，以 `参见 Epic [BR-01]` 格式引用，内容说明分配推荐依赖授权用户可查的评分结果与分级建议，其可见性要求与 Epic [BR-01] 一致。 |
| F-03 | R6 | 一般 | `anomaly-detection/README.md:验收标准:AC-04`、`assignment-recommendation/README.md:验收标准:AC-04` | F-02 AC-04 与 F-03 AC-04 定义了完全相同的验收场景：前置条件同为"异常线索处于待处置状态"、触发动作同为"分配推荐排序触发"、预期结果同为"该线索不出现在分配推荐队列中"，违反跨 Feature 验收标准无冗余重复定义的要求。异常线索对分配队列的排除规则在业务语义上属于 F-02（异常线索识别与复核）的输出约束，应在 F-02 中作为权威定义，F-03 仅需以前置条件方式引用该约束。 | 将 F-02 `anomaly-detection/README.md:验收标准:AC-04` 保留为权威定义；将 F-03 `assignment-recommendation/README.md:验收标准:AC-04` 修改为引用 F-02 输出约束的前置条件形式，例如将前置条件改为"待分配线索中不含未处置的异常线索（参见 F-02 AC-04 约束）"，删除 F-03 AC-04 中重复的预期结果描述。 |
| F-04 | R7 | 严重 | `lead-scoring/README.md:业务规则`、`lead-scoring/README.md:验收标准`、`anomaly-detection/README.md:业务规则`、`anomaly-detection/README.md:验收标准`、`assignment-recommendation/README.md:业务规则`、`assignment-recommendation/README.md:验收标准` | Epic [NFR-02]（信息脱敏传输）要求线索中含个人可识别信息的字段在传入外部 AI 推理服务前必须完成脱敏处理，标注适用 F-01、F-02、F-03。三个 Feature 的业务规则章节均未包含对 NFR-02 的引用或对应的脱敏约束 BR；验收标准章节均未包含验证 PII 字段脱敏的 AC。该信息安全约束完全遗漏于 Feature 层，下游 S0306 功能特性设计将无法获得脱敏的设计输入，存在个人数据保护合规风险，阻塞 F-01、F-02、F-03 的下游设计执行。 | 分别在 F-01、F-02、F-03 的业务规则章节中新增一条 BR，以 `参见 Epic [NFR-02]` 格式引用，明确本特性在调用外部 AI 推理服务前须完成 PII 字段脱敏的约束行为；同时在各 Feature 的验收标准章节中补充对应 AC，前置条件为"线索含个人可识别信息字段"、触发动作为"系统调用外部 AI 推理服务"、预期结果为"PII 字段在传出前已完成脱敏，脱敏后数据不含原始个人可识别内容"。 |
| F-05 | R7 | 一般 | `lead-scoring/README.md:验收标准` | Epic [NFR-01]（批量评分时效）要求单批次线索（≤500 条）从触发到结果全部就绪的业务感知等待时间不超过 30 秒。F-01 为批量评分能力的直接承载 Feature，其验收标准章节（AC-01 至 AC-06）均未包含性能时效验收条件，无法在 Feature 层验证 NFR-01 的时效要求是否满足，导致该非功能需求在设计阶段缺少验收依据。 | 在 F-01 `lead-scoring/README.md:验收标准` 中补充一条 AC，前置条件为"线索池中待评分新进线索数量不超过 500 条；外部 AI 推理服务可用"、触发动作为"MKT Leader 触发批量评分"、预期结果为"全部线索评分结果在触发后 30 秒内全部就绪，业务侧无需等待超出该时限（参见 Epic NFR-01）"，并关联 US-01。 |
| F-06 | R7 | 建议 | `lead-scoring/README.md:验收标准`、`anomaly-detection/README.md:验收标准`、`assignment-recommendation/README.md:验收标准` | Epic [NFR-03]（评分可审计）要求评分及分配推荐的所有操作均须留存完整审计日志，并支持按线索、操作人、时间范围检索。F-01 的 BR-03 与 AC-03 覆盖了评分版本记录的留存，F-03 的 BR-04 与 AC-03 覆盖了分配操作记录的留存，但三个 Feature 均未包含验证审计日志检索能力（按线索、操作人、时间范围查询）的 AC，NFR-03 的可查询性要求在 Feature 层未完整承接。 | 在 F-01 `lead-scoring/README.md:验收标准` 和 F-03 `assignment-recommendation/README.md:验收标准` 中各补充一条 AC，验证授权用户可按线索 ID、操作人、时间范围筛选并查询到对应的评分历史或分配操作审计记录（参见 Epic NFR-03）；F-02 可评估是否需要对处置操作审计同步补充检索 AC。 |
| F-07 | R2 | 建议 | `lead-scoring/README.md:特性概述.范围边界` | Epic [DEP-03]（T-01/E-03 下游消费）和 [DEP-04]（T-03/E-03 下游消费）标注影响 F-01，要求 F-01 评分模型变更时须提前通知下游协同确认。两项约束仅在 F-01 特性概述的"范围边界"第 4 条以引用形式记录，未在 F-01 业务规则章节中以 `参见 Epic [DEP-03]` / `参见 Epic [DEP-04]` 方式承接。根据 SOP R2 第 (4) 条映射，由于 A0304 模板无独立约束章节，Epic 级约束应在 Feature 业务规则中以引用方式承接，当前位置与 SOP 规定不符，下游消费约束在 BR 层无可见的追溯链路。 | 在 F-01 `lead-scoring/README.md:业务规则` 中补充一条 BR，以 `参见 Epic [DEP-03]` 和 `参见 Epic [DEP-04]` 格式引用，说明本特性输出的评分模型变更须提前通知 T-01/E-03 和 T-03/E-03 下游进行协同确认；特性概述中的范围边界第 4 条可保留作为范围说明，但 BR 层应同步承接以保证可追溯性。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-04 | 分别在 F-01 `lead-scoring/README.md:业务规则`、F-02 `anomaly-detection/README.md:业务规则`、F-03 `assignment-recommendation/README.md:业务规则` 中新增引用 `参见 Epic [NFR-02]` 的脱敏约束 BR；并在三个 Feature 的验收标准章节各补充一条验证 PII 字段脱敏的 AC（前置条件：含 PII 字段；触发：调用外部 AI 服务；预期：传出前已完成脱敏） | 产品负责人，执行 S0304 功能特性规划修订 | P0 | 待处理 |
| ACT-02 | F-01 | 在 F-01 `lead-scoring/README.md:业务规则` 中补充引用 `参见 Epic [ASM-01]` 的 BR（描述授权不可用时降级行为）；在 F-02 `anomaly-detection/README.md:业务规则` 和 F-03 `assignment-recommendation/README.md:业务规则` 中同步补充 `参见 Epic [ASM-01]` 引用 BR | 产品负责人，执行 S0304 功能特性规划修订 | P1 | 待处理 |
| ACT-03 | F-02 | 在 F-03 `assignment-recommendation/README.md:业务规则` 中新增一条 BR，以 `参见 Epic [BR-01]` 引用，说明分配推荐依赖授权用户可查的评分结果与分级建议 | 产品负责人，执行 S0304 功能特性规划修订 | P1 | 待处理 |
| ACT-04 | F-03 | 将 F-03 `assignment-recommendation/README.md:验收标准:AC-04` 修改为前置条件引用形式（参见 F-02 AC-04 约束），移除与 F-02 AC-04 重复的预期结果描述；保留 F-02 `anomaly-detection/README.md:验收标准:AC-04` 为权威定义 | 产品负责人，执行 S0304 功能特性规划修订 | P1 | 待处理 |
| ACT-05 | F-05 | 在 F-01 `lead-scoring/README.md:验收标准` 中补充一条性能时效 AC（≤500 条线索，触发后 30 秒内全部结果就绪，参见 Epic NFR-01），关联 US-01 | 产品负责人，执行 S0304 功能特性规划修订 | P1 | 待处理 |
| ACT-06 | F-06 | 在 F-01 `lead-scoring/README.md:验收标准` 和 F-03 `assignment-recommendation/README.md:验收标准` 中各补充一条审计日志可检索 AC，验证按线索 ID、操作人、时间范围查询的能力（参见 Epic NFR-03） | 产品负责人，执行 S0304 功能特性规划修订 | P2 | 待处理 |
| ACT-07 | F-07 | 在 F-01 `lead-scoring/README.md:业务规则` 中补充引用 `参见 Epic [DEP-03]` 和 `参见 Epic [DEP-04]` 的 BR，承接下游消费变更通知约束；特性概述范围边界第 4 条可保留 | 产品负责人，执行 S0304 功能特性规划修订 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 lead-scoring、F-02 anomaly-detection、F-03 assignment-recommendation）
- [x] R1 Feature 覆盖完备性检查已执行（3 个 Feature 文档均存在且章节完整，Epic 功能特性表与实际目录双向一致，无悬空引用）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：(1) 业务定义细化展开已验证；(2) 共享 BR 引用已验证，发现 F-01/F-02/F-03 未引用 ASM-01，记录为 F-01；(3) 场景步骤-US 覆盖已验证；(4) DEP/ASM 位置问题记录为 F-07）
- [x] R3 用户故事完备性检查已执行（Epic 场景一、场景二全部步骤均有 US 覆盖；US-AC 双向引用闭合；角色与 Epic 一致）
- [x] R4 BR 引用一致性检查已执行（共享 BR 识别：BR-01 适用 F-01/F-03、BR-05 适用 F-02/F-03；发现 F-03 未引用 Epic BR-01，记录为 F-02；"是否成立"类 BR 四要素已核验；BR 编号无跨 Feature 冲突）
- [x] R5 业务对象协调性检查已执行（三个 Feature 业务对象名称无重复，BR 引用的属性在对应业务对象定义中均存在，未发现实现层信息泄漏）
- [x] R6 验收标准协调性检查已执行（发现 F-02/F-03 AC-04 冗余重复，记录为 F-03；Happy Path 与异常路径覆盖已验证；AC 三要素完整性已核验）
- [x] R7 跨 Feature 一致性检查已执行（角色命名统一；依赖对称性：F-01 AC-04 引用 F-03 输出，F-03 范围已涵盖；范围覆盖：无遗漏无交叉；NFR 承接：NFR-02 遗漏记录为 F-04，NFR-01 缺 AC 记录为 F-05，NFR-03 检索能力记录为 F-06）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议（指明目标文件与章节）
- [x] 审核结论与问题统计数据一致（严重 1 条 → 不通过）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（F-01→ACT-02，F-02→ACT-03，F-03→ACT-04，F-04→ACT-01，F-05→ACT-05；建议级 F-06→ACT-06，F-07→ACT-07）
