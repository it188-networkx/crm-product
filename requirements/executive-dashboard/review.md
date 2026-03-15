---
description: "Theme Review（主题审核记录）模板，记录对指定需求主题内全部史诗定义的系统性审核结论与改进事项"
title: "Theme Review - [T-03] 决策驾驶舱 (Executive Dashboard)"
category: "Product Review"
version: "v1.0"
document_type: "theme-review"
author: "product-designer"
created_date: "2026-03-15"
last_updated: "2026-03-15"
status: "审核完成"
---

# Theme Review - [T-03] 决策驾驶舱 (Executive Dashboard)

## 审核摘要 (Review Summary)

**审核范围：** Theme [T-03] 决策驾驶舱 (Executive Dashboard)

**Theme 文档路径：** `requirements/executive-dashboard/README.md`

**审核输入文档清单：**

| 文档类型 | 路径 |
| :--- | :--- |
| A0302 需求主题定义 | `requirements/executive-dashboard/README.md` |
| A0303 需求史诗定义 | `requirements/executive-dashboard/funnel-analytics/README.md` |
| A0303 需求史诗定义 | `requirements/executive-dashboard/channel-roi/README.md` |
| A0303 需求史诗定义 | `requirements/executive-dashboard/opportunity-health/README.md` |
| A0303 需求史诗定义 | `requirements/executive-dashboard/go-nogo-dashboard/README.md` |

**审核结论：** 不通过

**问题统计：**

| 严重级别 | 数量 |
| :--- | :--- |
| 严重 | 1 |
| 一般 | 7 |
| 建议 | 2 |

## 评审明细 (Review Findings)

| Issue ID | 维度 | 严重级别 | 位置 | 问题描述 | 改进建议 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | R2 | 严重 | `requirements/executive-dashboard/README.md:史诗规划表` / `requirements/executive-dashboard/go-nogo-dashboard/README.md:概述.核心目标` | Theme 史诗规划表对 E-04 的业务定位描述为"按市场、渠道、阶段维度追踪 KPI 达成率，支持规则版本切换对比与历史回溯，帮助**管理层**判断当前**策略**是否继续执行或需调整"，主要用户为 CEO/管理层，聚焦宏观经营策略的 KPI 达成追踪。但 E-04 文档的核心目标实际定位为"为 **MKT Leader** 构建以**规则版本效果**为核心的'观测—对比—决策—回退'闭环"，主要用户偏移为 MKT Leader，核心 KPI（线索质量分布、跟进成功率、MQL→SQL 转化率）聚焦线索评分规则与培育触发规则的操作层效果，与 Theme 层描述的"按市场、渠道、阶段维度追踪 KPI 达成率"的宏观管理视角存在实质性偏差。Theme 层规划的管理层宏观 KPI 达成追踪能力（市场/渠道/阶段维度）未落在任何 Epic 的主体定位中，形成业务能力缺口。 | 优先与产品负责人及业务干系人对齐 E-04 的实际定位：若 E-04 聚焦规则效果的 MKT Leader 视角，须同步修订 `requirements/executive-dashboard/README.md` 史诗规划表中 E-04 的业务定位描述，并在史诗规划或拆分说明中明确说明宏观 KPI 达成率追踪如何被覆盖（新增 Epic 或并入现有 Epic）；若 E-04 应保留 CEO 宏观策略视角，须在 `requirements/executive-dashboard/go-nogo-dashboard/README.md` 中增加以 CEO 为主体的"查看市场/渠道/阶段 KPI 达成率"业务场景，并将 MKT Leader 规则效果评估明确定位为辅助能力或独立 Epic。 |
| F-02 | R2 | 一般 | `requirements/executive-dashboard/funnel-analytics/README.md:自检清单` / `requirements/executive-dashboard/channel-roi/README.md:自检清单` / `requirements/executive-dashboard/opportunity-health/README.md:自检清单` / `requirements/executive-dashboard/go-nogo-dashboard/README.md:自检清单` | Theme 验收标准（OC-01~OC-08）定义了本主题的上层交付约束，按 Theme->Epic Decomposition Contract 第 4 条映射规则，各 Epic 的自检清单应将 Theme OC 作为交付完整性的上层约束感知并引用。但现有 4 个 Epic 的自检清单均聚焦于 Epic 文档内部规范的完整性检查，未包含任何对 Theme 层 OC 的引用或覆盖性声明，导致 Epic 文档自检时无法验证其交付内容是否满足 Theme 级验收要求（例如 OC-01 漏斗数据同源、OC-03 ROI 口径可配置、OC-05 预警可追踪等）。 | 在各 Epic 的自检清单末尾补充"Theme 级 OC 覆盖声明"分组，逐条列出本 Epic 承接的 Theme OC 编号及覆盖说明。具体操作：(1) E-01 补充 OC-01、OC-02 的覆盖声明；(2) E-02 补充 OC-03、OC-04、OC-08 的覆盖声明；(3) E-03 补充 OC-05、OC-07 的覆盖声明；(4) E-04 补充 OC-06、OC-07 的覆盖声明。每条声明需指向本 Epic 中具体的 BR 或 Feature 编号作为落地依据。 |
| F-03 | R2 | 一般 | `requirements/executive-dashboard/opportunity-health/README.md:约束与依赖` / `requirements/executive-dashboard/go-nogo-dashboard/README.md:约束与依赖` | Theme 外部依赖概览中明确标注"全局审计日志能力"影响 E-03 与 E-04（缺失时"管理层操作与规则版本变更无法形成可追溯记录，GC-04 约束无法满足"）。按 Theme->Epic Decomposition Contract 第 5 条映射规则，该 Theme 级跨 Epic 依赖应在对应 Epic 中权威定义降级方案。但 E-03 的约束与依赖（DEP-01~DEP-04、ASM-01）中未将"全局审计日志能力"列为外部依赖，且无降级策略（E-03 BR-05 仅说明审计写入失败时"操作必须回滚"，属于应用层行为，非对基础审计能力缺失的降级方案）；E-04 的约束与依赖同样未声明审计能力依赖，BR-09 仅声明合规要求，无降级方案。 | 在 E-03 `requirements/executive-dashboard/opportunity-health/README.md` 的约束与依赖章节新增条目，例如`[DEP-05]全局审计日志`，明确依赖 GC-04 约定的审计日志基础能力，并定义降级策略（如：审计日志基础能力不可用时，CEO 的关注标记、转派操作仍可完成，但审计记录暂缓写入并在能力恢复后补写，同时在界面显示"操作已记录，审计延迟写入"提示）。在 E-04 约束与依赖章节同样新增对应条目，定义 Go/No-Go 决策与星标变更在审计能力缺失时的降级行为。 |
| F-04 | R3 | 一般 | `requirements/executive-dashboard/funnel-analytics/README.md:概述.价值预估` / `requirements/executive-dashboard/channel-roi/README.md:概述.价值预估` | Theme 价值承诺第一条"决策自主：老板通过系统做投入决策的事项占比从 0% 提升至 >= 60%（M6）"是以全体投入决策事项为分母的综合目标。E-01 价值预估声明"CEO 通过漏斗视图独立识别转化瓶颈并做出介入决策的事项占比从 0% 提升至 ≥ 60%（M6）"，E-02 价值预估声明"CEO 通过渠道 ROI 数据做渠道投入决策的事项占比从 0% 提升至 ≥ 60%（M6）"。两条 KPI 均采用相同的基准值（0%）和目标值（≥60%），但未说明各自适用的决策事项分母范围（E-01 分母为漏斗相关介入决策，E-02 分母为渠道投入决策），也未标注两 Epic 各自对 Theme 综合目标 60% 的独立分担比例，导致若合并计算时存在加总重叠或口径混淆的风险。 | 在 E-01 和 E-02 的价值预估中明确各自的 KPI 分母范围与对 Theme 综合目标的分担口径。例如：E-01 修订为"CEO 通过漏斗视图识别转化瓶颈并做出介入决策的比例达到 ≥ 60%（M6），此为 Theme KPI 中**漏斗介入类**决策事项的分贡献口径"；E-02 修订为"CEO 通过渠道 ROI 数据做渠道资源配置决策的比例达到 ≥ 60%（M6），此为 Theme KPI 中**渠道资源类**决策事项的分贡献口径"。同时在 Theme A0302 的价值承诺处补注各类决策事项的分类口径说明，避免合并统计时产生重复计算。 |
| F-05 | R3 | 一般 | `requirements/executive-dashboard/go-nogo-dashboard/README.md:概述.价值预估` | E-04 的两条价值预估 KPI 均标注`[推导-待确认]`，且核心 KPI 的"具体计算口径与目标值需与 MKT Leader 和 CEO 访谈确认"（文档原文标注为`[缺少需求输入-待补充]`）。同时，Theme 价值承诺第二条"介入及时：高风险商机感知时延 ≤ 24 小时"在 E-04 的价值预估中完全未承接（E-03 承接了该 KPI，E-04 未声明其与此 Theme KPI 的关系，且 E-04 实际聚焦规则效果，确实不直接承接此 KPI，但应明确说明）。在缺乏具体 KPI 目标值的情况下，E-04 对 Theme 价值承诺的实质贡献无法量化核验，影响 Theme 层 KPI 覆盖的完整性置信度。 | 在 M2 Sprint 规划前完成 MKT Leader 与 CEO 的 KPI 访谈（参照 E-04 文档中待办说明），将具体 KPI 计算口径与目标值补入 `requirements/executive-dashboard/go-nogo-dashboard/README.md` 概述.价值预估章节，并明确标注与 Theme 两条核心 KPI 的承接关系或不承接原因（如 E-04 主要支撑 Theme KPI1 的规则优化路径，不直接承接 KPI2，应在文档中显式说明）。 |
| F-06 | R4 | 一般 | `requirements/executive-dashboard/README.md:用户旅程 CEO/买单方旅程 节点G` / `requirements/executive-dashboard/go-nogo-dashboard/README.md:业务场景` | Theme CEO 旅程节点 G 为"E-04: 查看 KPI 达成率与规则效果对比"，旅程图中该节点的触发路径来自 D（E-03 调整渠道资源），说明 CEO 在评估策略效果时需查看 E-04 看板。但 E-04 的两个业务场景均以 MKT Leader 为主体（场景一：MKT Leader 评估新线索评分规则；场景二：MKT Leader 发现规则效果下降并回退），E-04 BR-06 明确说明"CEO 角色为只读查看，不具备决策写权限"。CEO 在 E-04 的角色未被任何业务场景描述所承接，Theme 旅程中 CEO 通过 E-04 做"策略继续或调整"判断的业务闭环在 E-04 文档中找不到对应的步骤描述。 | 在 `requirements/executive-dashboard/go-nogo-dashboard/README.md` 的业务场景章节补充"场景三：CEO 只读查看规则效果达成情况"，以 CEO 为主体描述其通过 E-04 看板查阅当前规则效果 KPI 并判断是否需要指示 MKT Leader 调整策略的业务流程，与 Theme 旅程节点 G 形成闭环承接。或者，若 E-04 定位确认为 MKT Leader 专属工具，则修订 Theme 用户旅程，将节点 G 的 Epic 引用修订为更准确的描述，并补充 CEO 策略判断所需的视图来源。 |
| F-07 | R6 | 一般 | `requirements/executive-dashboard/channel-roi/README.md:功能特性` / `requirements/executive-dashboard/channel-roi/README.md:业务场景` | E-02 功能特性 F-04（ROI 公式配置管理）在两个业务场景（场景一：季度渠道投入复盘；场景二：内容选题效果追踪）中均无对应步骤引用，两个场景的参与角色为 CEO 与市场负责人，均为数据消费者而非配置者。F-04 涉及的业务能力（ROI 口径创建、审批、版本管理）是 ROI 数据可信性的前提，但缺少描述管理员或产品负责人完成 ROI 口径配置全流程的业务场景，导致 F-04 的业务必要性与操作路径无法从场景层面验证，Feature 清单与场景覆盖之间存在缺口。 | 在 `requirements/executive-dashboard/channel-roi/README.md` 的业务场景章节新增"场景三：产品管理员配置 ROI 计算口径"，以管理员/CRM 产品负责人为主体，描述创建 ROI 口径配置、设置归因模型与成本口径、发起审批并生效的完整业务流程，引用 F-04 特性。该场景可定性为支撑型场景（非主线用户旅程），但须在文档中明确出现以保证 Feature 清单完备性。 |
| F-08 | R6 | 一般 | `requirements/executive-dashboard/channel-roi/README.md:功能特性 F-01 范围说明` / `requirements/executive-dashboard/channel-roi/README.md:功能特性 F-04 范围说明` | E-02 F-01（渠道 ROI 总览与对比）的范围说明包含"ROI 计算口径支持管理员配置"，与 F-04（ROI 公式配置管理）的核心能力（"提供 ROI 计算口径……的创建、审批与版本管理"）在"ROI 口径配置"这一业务能力上存在描述重叠，边界不清晰。F-01 是数据展示与对比 Feature，配置能力不应在其范围说明中声明所有权；若 F-01 的范围说明意指"F-01 依赖已配置的口径呈现数据"，则应改为依赖性描述，而非范围声明。 | 修订 `requirements/executive-dashboard/channel-roi/README.md` 中 F-01 的范围说明，将"ROI 计算口径支持管理员配置"改为依赖性声明，例如"ROI 展示口径来源于 F-04 中管理员预设的计算规则，F-01 不自行承担口径定义能力"，从而明确 F-01 的范围止于"展示、对比与时间窗口切换"，ROI 口径配置的所有权归属 F-04，消除两 Feature 的描述重叠。 |
| F-09 | R2 | 建议 | `requirements/executive-dashboard/channel-roi/README.md:概述.核心目标` | E-02 的核心目标（"本 Epic 旨在构建各渠道线索量、转化率与商机价值的量化对比视图，并含内容主题归因分析，让 CEO 基于可信数据做出渠道加码或收缩与内容选题聚焦的资源分配决策"）与 Theme 史诗规划表中 E-02 的业务定位描述（"量化各渠道的线索量、转化率与商机价值，含内容主题归因分析，支持 CEO 做出有依据的渠道与内容资源分配决策"）高度相似，基本为原文复述，未体现 Epic 层对 Theme 业务定位的进一步细化展开，例如缺少对具体能力边界的说明（多渠道横向对比的维度构成、归因模型范围、内容主题归因链路起点等）。 | 在 `requirements/executive-dashboard/channel-roi/README.md` 的核心目标中补充能力边界细化，具体可增加：支持多渠道横向 ROI 对比（含多归因模型切换）、内容主题归因链路起点为曝光、依赖管理员预置的 ROI 口径保证数据可信性等说明，使核心目标成为对 Theme 业务定位的展开细化而非复述。 |
| F-10 | R5 | 建议 | `requirements/executive-dashboard/opportunity-health/README.md:业务场景 场景一步骤4/场景二步骤4-5` | E-03 业务场景（场景一步骤 4 "转派，指定新的销售负责人"、场景二步骤 4-5 "新受让销售负责人"）引入了"销售负责人"这一角色，该角色在 Theme 用户旅程（CEO/买单方旅程、市场负责人旅程）中均未定义。根据 SOP R5 规则，Theme 层面未定义的新角色需确认是否为有意引入。"销售负责人"在 E-03 中作为被转派通知对象出现，是预警处置业务流程的必要角色，其引入逻辑合理，但应在文档中明确说明。 | 在 `requirements/executive-dashboard/opportunity-health/README.md` 的业务场景章节（或概述业务背景）中补充说明："销售负责人作为预警处置流程的被动响应角色，仅在转派通知场景中被引用，不作为驾驶舱的主动操作角色；该角色的身份与组织归属与 T-01 线索分配模块保持一致。"同时建议在 Theme A0302 文档的跨 Epic 公共约定中增加对"销售负责人"角色的简要定义，以保持跨 Epic 角色命名的一致性。 |

## 改进事项 (Action Items)

| Action ID | 关联 Issue | 责任归属 | 建议优先级 | 状态 |
| :--- | :--- | :--- | :--- | :--- |
| ACT-01 | F-01 | 产品负责人（与业务干系人对齐 E-04 定位后，修订 `requirements/executive-dashboard/README.md` 史诗规划表或 `go-nogo-dashboard/README.md` 核心目标，执行 [S0302] 或 [S0303] 变更） | P0 | 待处理 |
| ACT-02 | F-02 | 产品负责人（修订全部 4 个 Epic 的自检清单，补充 Theme OC 覆盖声明，执行 [S0303] 更新对应 Epic 文档） | P1 | 待处理 |
| ACT-03 | F-03 | 产品负责人（在 E-03 和 E-04 的约束与依赖章节新增全局审计日志能力依赖条目及降级方案，执行 [S0303] 更新对应 Epic 文档） | P1 | 待处理 |
| ACT-04 | F-04 | 产品负责人（明确 E-01 与 E-02 价值预估 KPI 的分担口径，并在 Theme A0302 价值承诺处补注口径说明，执行 [S0302]、[S0303] 更新对应文档） | P1 | 待处理 |
| ACT-05 | F-05 | 产品负责人（完成 MKT Leader/CEO 访谈，补充 E-04 价值预估具体 KPI 目标值，明确与 Theme KPI 的承接关系，执行 [S0303] 更新 E-04 文档） | P1 | 待处理 |
| ACT-06 | F-06 | 产品负责人（在 E-04 文档中补充以 CEO 为主体的查阅场景，或修订 Theme 用户旅程节点 G 的描述，执行 [S0302] 或 [S0303] 更新对应文档） | P1 | 待处理 |
| ACT-07 | F-07 | 产品负责人（在 E-02 文档中新增管理员配置 ROI 口径的业务场景，执行 [S0303] 更新 `channel-roi/README.md`） | P1 | 待处理 |
| ACT-08 | F-08 | 产品负责人（修订 E-02 F-01 范围说明，消除与 F-04 的描述重叠，执行 [S0303] 更新 `channel-roi/README.md`） | P1 | 待处理 |
| ACT-09 | F-09 | 产品负责人（补充 E-02 核心目标的细化展开内容，执行 [S0303] 更新 `channel-roi/README.md`） | P2 | 待处理 |
| ACT-10 | F-10 | 产品负责人（在 E-03 文档或 Theme 文档中补充"销售负责人"角色说明，执行 [S0303] 或 [S0302] 更新对应文档） | P2 | 待处理 |

## 自检清单 (Self-Check)

- [x] 已读取 Theme 文档（A0302）全文
- [x] 已读取该 Theme 下全部 Epic 文档（A0303）全文（E-01/E-02/E-03/E-04 共 4 份）
- [x] R1 Epic 覆盖完备性检查已执行（4 个 Epic 文档均存在且链接可达；各 Epic Feature 数量均 >= 2；无悬空引用）
- [x] R2 向下拆分契约兑现检查已执行（5 条映射逐条核验：(1) 业务定位->核心目标；(2) 价值承诺->价值预估；(3) 用户旅程->业务场景；(4) 验收标准 OC->自检清单；(5) 外部依赖->降级方案）
- [x] R3 价值指标协调性检查已执行（KPI 覆盖、量级、口径逐条核验，识别 E-01/E-02 重叠计算风险与 E-04 KPI 缺失问题）
- [x] R4 用户旅程覆盖度检查已执行（CEO 旅程与市场负责人旅程各节点逐一核验；跨 Epic 业务约束覆盖情况核验）
- [x] R5 跨 Epic 一致性检查已执行（角色命名、编号唯一性、依赖对称性、范围覆盖逐项核验）
- [x] R6 Feature 清单完备性检查已执行（Feature 数量、信息完整性、场景覆盖、范围重叠逐 Epic 核验）
- [x] 每条发现均引用具体文件路径与章节
- [x] 每条发现均给出可执行的改进建议
- [x] 审核结论与问题统计数据一致（严重 1 条 -> 不通过）
- [x] 改进事项已为每条一般/严重级别的发现创建 Action（F-01~F-08 对应 ACT-01~ACT-08；F-09~F-10 为建议级别，创建 ACT-09~ACT-10）
