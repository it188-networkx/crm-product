---
description: "Epic Review（史诗审核记录），记录对 E-03「AI 知识向量化引用」Epic 定义（A0303）及其全部下属 Feature（A0304）的系统性审核结论与改进事项"
title: "Epic Review - [T-04/E-03] AI 知识向量化引用 (Knowledge Vectorization)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Epic Review - [T-04/E-03] AI 知识向量化引用 (Knowledge Vectorization)

## 审核摘要 (Review Summary)

**审核范围：** Epic [T-04/E-03] AI 知识向量化引用（所属 Theme: [T-04] 知识库；路径：`requirements/knowledge-repository/knowledge-vectorization/`）

**Epic 文档路径：** `requirements/knowledge-repository/knowledge-vectorization/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 | 状态 |
| :--- | :--- | :--- |
| A0303 需求史诗定义 | `requirements/knowledge-repository/knowledge-vectorization/README.md` | 已读取 |
| A0304 需求特性定义（F-01） | `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md` | 已读取 |
| A0304 需求特性定义（F-02） | `requirements/knowledge-repository/knowledge-vectorization/semantic-retrieval/README.md` | 文档缺失 |
| A0304 需求特性定义（F-03） | `requirements/knowledge-repository/knowledge-vectorization/feedback-loop/README.md` | 文档缺失 |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 2 |
| 一般 | 2 |
| 建议 | 2 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R1 | 严重 | `requirements/knowledge-repository/knowledge-vectorization/`（目录级） | Epic 功能特性表列出 F-02「知识语义检索与来源标注」，文档路径为 `semantic-retrieval/README.md`，但该目录不存在，文档未建立。Epic 业务场景一步骤 3-4 与场景三步骤 3 均归属 F-02，F-02 缺失导致这些场景步骤在 Feature 层无任何覆盖。 | 按 S0304 功能特性规划为 F-02 创建完整的 A0304 文档（`requirements/knowledge-repository/knowledge-vectorization/semantic-retrieval/README.md`），覆盖语义检索、Top-K 结果返回、来源元数据标注与历史建议下线标注等范围，并承接 Epic BR-02（部分）、BR-04、BR-05、BR-06 与 NFR-02。 |
| F-02 | R1 | 严重 | `requirements/knowledge-repository/knowledge-vectorization/`（目录级） | Epic 功能特性表列出 F-03「引用质量反馈闭环」，文档路径为 `feedback-loop/README.md`，但该目录不存在，文档未建立。Epic 业务场景二（售前对 AI 引用知识提交质量反馈）的全部步骤归属 F-03，F-03 缺失导致该完整业务场景在 Feature 层无任何覆盖。 | 按 S0304 功能特性规划为 F-03 创建完整的 A0304 文档（`requirements/knowledge-repository/knowledge-vectorization/feedback-loop/README.md`），覆盖反馈提交、反馈与知识单元 ID 关联、阈值累计通知与 E-01 事件推送等范围，并承接 Epic BR-07 与 DEP-04。 |
| F-03 | R6 | 一般 | `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:验收标准` | F-01 局部 BR-02（版本迭代处理）要求"知识单元版本升级时，前一版本对应向量条目在新版本向量化完成后标记为下线，同一知识单元的不同版本向量条目不得同时处于'检索就绪'状态"，但验收标准五条（AC-01 至 AC-05）中无任何 AC 覆盖该版本升级场景（前提：同一知识单元已有检索就绪向量条目；触发：发布新版本事件；预期：新版本入库且旧版本下线），BR-02 的核心约束无测试验证闭合口径。 | 在 `vectorization-pipeline/README.md:验收标准` 中补充一条 AC，明确前置条件（同一知识单元 ID 已存在"检索就绪"向量条目）、触发动作（E-01 发出该知识单元新版本的发布事件）、预期结果（新版本向量条目创建并标记为"检索就绪"；旧版本向量条目标记为"已下线"；同一时刻该知识单元仅有一条"检索就绪"向量条目），并在用户故事 US-01 的 AC Ref 中关联该新 AC。 |
| F-04 | R7 | 一般 | `requirements/knowledge-repository/knowledge-vectorization/README.md:非功能需求` / `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md` | Epic NFR-02 规定"语义检索（Top-K=5）业务感知延迟不超过 500ms（P95），不阻塞下游 AI 建议生成主路径"，该 NFR 应由 F-02 在验收标准与业务规则中承接。因 F-02 文档缺失，NFR-02 在全部已建立的 Feature 层文档中均无承接，导致 Epic 级性能约束无 Feature 层验证口径。 | 在 F-02（`semantic-retrieval/README.md`）创建时，须在其验收标准中显式覆盖 NFR-02 性能要求（Top-K=5，P95 ≤ 500ms），并在 F-02 业务规则中以"参见 Epic [NFR-02]"标注引用。当前 F-04 发现可在 F-02 文档建立并完成 R7 复审后关闭。 |
| F-05 | R4 | 建议 | `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:验收标准` | F-01 局部 BR 编号（BR-01 幂等性、BR-02 版本迭代、BR-03 软删除完整性）与 Epic 层 BR 编号（BR-01 发布门禁、BR-02 归档联动下线、BR-03 失败阻断）完全重叠。AC-02 引用"参见 BR-03"、AC-04 引用"参见 BR-01"时均未标注"本 Feature"或"Epic"前缀，读者无法直接判断引用的是 Feature 局部 BR 还是 Epic 同号 BR，违反引用一致性原则（Epic BR 引用已用"参见 Epic [BR-xx]"格式，局部引用格式未区分）。 | 将 `vectorization-pipeline/README.md:验收标准` 中所有局部 BR 的引用格式统一改为"参见本 Feature [BR-xx]"（例：AC-02 中"参见 BR-03"改为"参见本 Feature [BR-03]"；AC-04 中"参见 BR-01"改为"参见本 Feature [BR-01]"），与"参见 Epic [BR-xx]"格式形成明确区分。 |
| F-06 | R7 | 建议 | `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:业务规则 / 验收标准` | Epic NFR-03 要求"向量化任务执行日志（含触发事件、入库状态、失败原因）保留不少于 12 个月，支持按知识单元 ID、时间范围检索"。F-01 局部 BR-03（软删除完整性）已通过"以满足 Epic [NFR-03] 规定的不少于 12 个月审计追溯要求"引用承接，但 F-01 验收标准中无 AC 验证该审计可检索性约束，NFR-03 在 Feature 层仅有 BR 引用而无验证闭合。 | 在 `vectorization-pipeline/README.md:验收标准` 中补充 AC，覆盖向量条目软删除后记录可按 NFR-03 规定的检索维度（知识单元 ID、时间范围）被查询到的场景，关联局部 BR-03。若该 AC 在当前迭代难以测试（属基础设施级约束），可在 AC 预期结果中注明"通过运营查询接口或管理后台验证"。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 按 S0304 功能特性规划，新建 `requirements/knowledge-repository/knowledge-vectorization/semantic-retrieval/README.md`，补全 F-02「知识语义检索与来源标注」的完整 A0304 文档，覆盖用户故事、业务规则（承接 Epic BR-02 部分、BR-04、BR-05、BR-06）、业务对象定义与验收标准，并在验收标准中承接 NFR-02 性能约束 | 产品负责人（执行 S0304） | P0 | 待处理 |
| ACT-02 | F-02 | 按 S0304 功能特性规划，新建 `requirements/knowledge-repository/knowledge-vectorization/feedback-loop/README.md`，补全 F-03「引用质量反馈闭环」的完整 A0304 文档，覆盖用户故事、业务规则（承接 Epic BR-07、DEP-04）、业务对象定义与验收标准 | 产品负责人（执行 S0304） | P0 | 待处理 |
| ACT-03 | F-03 | 在 `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:验收标准` 中补充知识单元版本升级场景 AC（前置条件：同一 ID 已有"检索就绪"条目；触发：新版本发布事件；预期：新版本入库且旧版本下线，同时仅有一条就绪条目），并在 US-01 的 AC Ref 中关联该 AC | 产品负责人 | P1 | 待处理 |
| ACT-04 | F-04 | F-02 文档建立后，在 `semantic-retrieval/README.md:验收标准` 中显式覆盖 NFR-02（Top-K=5，P95 ≤ 500ms），并在业务规则中以"参见 Epic [NFR-02]"引用；ACT-01 完成后由产品负责人在 F-02 复审时验证关闭 | 产品负责人 | P1 | 待处理 |
| ACT-05 | F-05 | 将 `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:验收标准` 中局部 BR 引用格式统一改为"参见本 Feature [BR-xx]"（AC-02 中"参见 BR-03"、AC-04 中"参见 BR-01"均需更新），与"参见 Epic [BR-xx]"格式形成一致区分 | 产品负责人 | P2 | 待处理 |
| ACT-06 | F-06 | 在 `requirements/knowledge-repository/knowledge-vectorization/vectorization-pipeline/README.md:验收标准` 中补充 NFR-03 审计可检索性 AC，关联 F-01 局部 BR-03（软删除完整性） | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文（`requirements/knowledge-repository/knowledge-vectorization/README.md`，v1.1）
- [x] 已读取该 Epic 下全部可达 Feature 文档（A0304）全文（F-01 `vectorization-pipeline/README.md` 已读取；F-02、F-03 文档缺失，已在 R1 记录严重发现）
- [x] R1 Feature 覆盖完备性检查已执行（正向：Epic 3 个 Feature，F-01 文档存在，F-02/F-03 文档缺失；反向：已存在文档均在 Epic 索引中）
- [x] R2 向下拆分契约兑现检查已执行（针对 F-01：4 条映射逐条核验通过；F-02/F-03 因文档缺失降级）
- [x] R3 用户故事完备性检查已执行（F-01：US-AC 双向追溯完整，Epic 场景步骤覆盖完整，角色一致；F-02/F-03 因文档缺失降级）
- [x] R4 BR 引用一致性检查已执行（F-01：Epic 共享 BR 正确引用，局部 BR 无矛盾；发现局部 BR 编号与 Epic BR 编号重叠导致 AC 引用歧义，已记录为建议级发现 F-05）
- [x] R5 业务对象协调性检查已执行（F-01：两个业务对象（向量化任务、向量条目）属性完整、状态语义清晰、无实现侧信息泄漏；F-02/F-03 因文档缺失无法跨 Feature 比对）
- [x] R6 验收标准协调性检查已执行（F-01：Happy Path 与异常路径覆盖，发现版本升级场景 AC 缺失，已记录为一般级发现 F-03；AC 三要素完整；BR 引用闭合）
- [x] R7 跨 Feature 一致性检查已执行（角色一致；编号唯一；范围覆盖分析：F-01 覆盖向量化管线，F-02/F-03 未建立文档；NFR 承接：NFR-01 在 F-01 AC-01 中承接，NFR-02 无承接（F-04 发现），NFR-03 仅 BR 引用承接（F-06 发现））
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致（严重 2 条 -> 不通过；严重 2 + 一般 2 + 建议 2 共 6 条与评审明细行数吻合）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（F-01 -> ACT-01；F-02 -> ACT-02；F-03 -> ACT-03；F-04 -> ACT-04）
