---
description: "Epic Review（史诗审核记录），记录对 T-03/E-03 商机健康度预警全部特性定义的系统性审核结论与改进事项"
title: "Epic Review - [E-03] 商机健康度预警 (Opportunity Health)"
category: "Product Review"
version: "v1.0"
document_type: "epic-review"
author: "product-reviewer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "有条件通过"
---

# Epic Review - [E-03] 商机健康度预警 (Opportunity Health)

## 审核摘要 (Review Summary)

**审核范围：** Epic [E-03] 商机健康度预警（所属 Theme: T-03 CEO 决策驾驶舱）

**Epic 文档路径：** `requirements/executive-dashboard/opportunity-health/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0303 需求史诗定义 | `requirements/executive-dashboard/opportunity-health/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/opportunity-health/health-scoring/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/opportunity-health/risk-alert-list/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/opportunity-health/alert-action/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/opportunity-health/alert-push/README.md` |
| A0304 需求特性定义 | `requirements/executive-dashboard/opportunity-health/competitive-threat-tracking/README.md` |

**审核结论：** 有条件通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 0 |
| 一般 | 2 |
| 建议 | 3 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R5 | 一般 | `health-scoring/README.md:业务对象定义:商机健康度评分记录` | F-01 BR-06 明确要求每次评估结论须包含"三个维度得分**及其对应权重**"，但业务对象`商机健康度评分记录`中仅定义了`漏斗停滞得分`、`AI 评分得分`、`跟进行为得分`三个维度得分字段，缺少"维度权重"或"权重版本引用"属性。现有`阈值版本引用`属性可间接追溯到`健康度阈值配置.高风险阈值边界（含各维度权重）`，但并不满足 BR-06 要求评估结论**直接包含**权重的表述。下游 S0306 设计人员据此业务对象设计时，将无法确定评估结论是否需要存储各维度权重快照。 | 在`health-scoring/README.md`的业务对象`商机健康度评分记录`中补充"各维度权重快照"属性（含三个维度的当次权重值），或将 BR-06 的措辞修改为"含各维度得分及权重版本引用"，并在属性说明中注明权重通过`阈值版本引用`间接追溯，确保 BR-06 与业务对象定义的表述口径完全一致。 |
| F-02 | R4 | 一般 | `alert-push/README.md:业务规则:BR-06` / `alert-push/README.md:验收标准:AC-01,AC-02` | F-04 BR-06 在同一条规则中先给出"5 分钟内"的具体数值，紧接着又标注"TBD 具体时限，责任归属：产品负责人"，二者在逻辑上相互矛盾：若时限为 TBD 则 BR-06 不构成可测试的判定条件，若时限已确定为 5 分钟则不应标注 TBD。AC-01 和 AC-02 直接引用"5 分钟内"作为可测试验收阈值，与 BR-06 的 TBD 标注形成内在矛盾——若产品负责人后续将时限调整为其他值，BR-06 与 AC-01、AC-02 须同步修改，但目前无机制保障两者一致性。该矛盾使 BR-06 的四要素中"判定阈值"处于不确定状态，不符合可测试业务规则的基本要求。 | 产品负责人在 M3 Sprint 规划前完成时限确认后，按以下方式之一处理：（a）若时限确认为 5 分钟，去掉 BR-06 中"TBD"标注，使 BR-06 成为确定性规则；（b）若时限尚未确认，将 BR-06 中的"5 分钟内"替换为"[TBD，待产品负责人确认]"，并将 AC-01、AC-02 中的"5 分钟内"改为"在 BR-06 定义的时限内"，保持 BR 与 AC 口径的动态一致性。 |
| F-03 | R7 | 建议 | `alert-push/README.md:特性概述:范围边界` / `competitive-threat-tracking/README.md:特性概述:范围边界` | F-04 范围边界声明"竞品威胁信号的采集与关联逻辑（参见 F-05，上游信号来自 T-02/E-03，参见 Epic [DEP-03]）"，明确依赖 F-05 执行信号与商机的关联处理；F-04 BR-02 的触发条件为"T-02/E-03 提供的竞品威胁等级在本 Epic 关联的商机维度发生等级上升"，这同样依赖 F-05 产出的`竞品威胁商机关联记录`。然而 F-05 的范围边界仅描述"包含：竞品威胁信号与在途商机的关联展示"，未明确声明"向 F-04 提供竞品威胁等级变更事件以支撑推送触发"。此依赖关系目前为单向声明（F-04 引用 F-05，F-05 未声明此输出），在 S0306 设计阶段可能引发两个 Feature 之间的边界争议，需提前明确谁负责产出"等级变更事件"。 | 在`competitive-threat-tracking/README.md`范围边界的"包含"项中补充"向 F-04 提供竞品威胁等级变更事件"，或在"不包含"项中明确"主动推送通知（参见 F-04）由 F-04 消费本特性的关联记录等级变更事件触发"，使 F-04 对 F-05 的依赖关系在两侧范围边界中均有显式对称声明。 |
| F-04 | R3 | 建议 | `health-scoring/README.md:用户故事:US-03` | F-01 US-03 引入了"产品管理员"角色（"按客户类型分别配置健康度等级阈值"），但 Epic 业务场景（场景一、场景二）仅定义 CEO 和销售负责人两个角色。产品管理员虽在 Epic BR-04 中有隐式引用（"风险等级判定阈值由产品管理员在系统设置页配置"），但 Epic 未在业务场景中为其设置专属场景步骤。US-03 缺乏场景层级的溯源依据，使该用户故事与 Epic 业务场景的可追溯链路断开，在后续 Epic 迭代或主题级审核时容易被遗漏。 | 在`requirements/executive-dashboard/opportunity-health/README.md`的业务场景章节中补充一个场景（如"场景三：产品管理员配置健康度阈值"）或在现有场景的前置步骤中加入阈值配置引用；或在 F-01 US-03 的说明中通过"参见 Epic [BR-04]"明确此用户故事的溯源来自 Epic BR-04 而非业务场景，使角色引入有明确依据。 |
| F-05 | R5 | 建议 | `alert-push/README.md:业务对象定义:预警推送通知记录` | F-04 业务对象`预警推送通知记录`中"商机摘要"属性的字段说明为"通知内含的商机关键信息（名称、客户、负责人、等级、风险类型）"，但 F-04 BR-03 要求通知内容必须包含"商机名称、客户名称、**客户类型**、当前负责人、健康度等级（或竞品威胁等级）、主要风险类型标记、直达处置操作的入口"。"商机摘要"字段描述遗漏了"客户类型"这一在 BR-03 中被明确要求的字段，导致业务对象定义与 BR 的内容不一致，S0306 设计人员依据业务对象定义设计通知字段时可能遗漏客户类型。 | 在`alert-push/README.md`业务对象`预警推送通知记录.商机摘要`的字段说明中补充"客户类型"，使字段枚举与 BR-03 完全对齐：商机名称、客户名称、客户类型、当前负责人、健康度/竞品威胁等级、主要风险类型。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 修改内容 | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 在`health-scoring/README.md`的业务对象`商机健康度评分记录`中补充"各维度权重快照"属性，或修改 BR-06 措辞为"含权重版本引用"，确保 BR-06 与业务对象定义口径一致 | 产品负责人 | P1 | 待处理 |
| ACT-02 | F-02 | 产品负责人确认推送时限后，在`alert-push/README.md`中统一 BR-06 与 AC-01、AC-02 的时限表述，去掉"TBD"或统一替换为引用 BR-06 时限占位符 | 产品负责人 | P1 | 待处理 |
| ACT-03 | F-03 | 在`competitive-threat-tracking/README.md`范围边界的"包含"项中补充"向 F-04 提供竞品威胁等级变更事件"，明确 F-04 依赖的输出方 | 产品负责人 | P2 | 待处理 |
| ACT-04 | F-04 | 在 Epic README 的业务场景章节中补充产品管理员的操作场景，或在`health-scoring/README.md` US-03 中补充"参见 Epic [BR-04]"的溯源说明 | 产品负责人 | P2 | 待处理 |
| ACT-05 | F-05 | 在`alert-push/README.md`业务对象`预警推送通知记录.商机摘要`字段说明中补充"客户类型"，与 BR-03 枚举完全对齐 | 产品负责人 | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Epic 文档（A0303）全文
- [x] 已读取该 Epic 下全部 Feature 文档（A0304）全文（F-01 health-scoring / F-02 risk-alert-list / F-03 alert-action / F-04 alert-push / F-05 competitive-threat-tracking，共 5 份）
- [x] R1 Feature 覆盖完备性检查已执行（Epic 功能特性表 5 个 Feature 与实际目录 5 个子目录一一对应，无悬空引用；全部 Feature 文档用户故事、业务规则、验收标准章节均存在且非空）
- [x] R2 向下拆分契约兑现检查已执行（4 条映射逐条核验：范围说明 -> 业务定义均为实质细化展开；共享 BR 均通过"参见 Epic [BR-xx]"正确引用；业务场景步骤 -> 用户故事覆盖完整；DEP/ASM -> 业务规则均在相关 Feature 中承接）
- [x] R3 用户故事完备性检查已执行（场景一/二全部步骤 -> US 覆盖无遗漏；US-AC 双向引用闭合；角色使用情况已核查，产品管理员角色有建议级发现）
- [x] R4 BR 引用一致性检查已执行（共享 BR 识别并逐 Feature 检查引用正确性；发现 F-04 BR-06 TBD 与 AC 数值矛盾，记录为一般级别发现；BR 编号局部编号机制符合规范，无全局冲突）
- [x] R5 业务对象协调性检查已执行（跨 Feature 共享状态名称一致；发现 F-01 商机健康度评分记录缺少维度权重属性，记录为一般级别发现；F-04 商机摘要字段描述缺少客户类型，记录为建议级别发现；无实现侧词汇泄漏）
- [x] R6 验收标准协调性检查已执行（跨 Feature AC 无冗余冲突；各 Feature 均覆盖 Happy Path、异常路径、边界条件；AC 三要素完整；AC 中 BR 引用编号均存在且语义匹配）
- [x] R7 跨 Feature 一致性检查已执行（角色命名跨 Feature 统一；F-04 对 F-05 的依赖单向声明问题记录为建议级别发现；范围覆盖无交叉无遗漏；NFR-01 -> F-02、NFR-02 -> F-04/F-05、NFR-03 -> F-03 均已承接）
- [x] 每条发现均引用具体文件路径与章节位置
- [x] 每条发现均给出可执行的改进建议（指明目标文件与章节）
- [x] 审核结论与问题统计数据一致（0 严重、2 一般、3 建议 -> 有条件通过）
- [x] 改进事项已为每条严重/一般级别的发现创建 Action（ACT-01 对应 F-01，ACT-02 对应 F-02）
