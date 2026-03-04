## 目录结构

产品级文档，跨 Feature 聚合提炼系统级技术上下文，产出系统架构与架构决策，设计背景并入架构设计文档。

```text
architecture/
├── architecture.md             # 系统架构 (产品级)
├── capacity.md                 # 容量规划方案 (产品级)
├── high-availability.md        # 高可用容错方案 (产品级)
├── security.md                 # 安全防护方案 (产品级)
├── observability.md            # 可观测性方案 (产品级)
└── adrs/                       # 架构决策记录 (实例级)
    └── adrNNN-<topic>.md
```

## 工作流程

### 架构设计

```mermaid
%%{init: {'flowchart': {'padding': 8, 'nodeSpacing': 32, 'rankSpacing': 32}} }%%
graph TD
    classDef sop fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E3A5F,rx:8,ry:8
    classDef art fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F
    classDef ext fill:#EDE9FE,stroke:#7C3AED,stroke-width:1.5px,color:#4C1D95
    classDef dat fill:#F0FDF4,stroke:#16A34A,stroke-width:1.5px,color:#14532D

    A0203["A0203 产品定义文档"]:::ext
    A0301["A0301 产品需求大纲"]:::ext
    A0302["A0302 需求主题定义"]:::ext
    A0303["A0303 需求史诗定义"]:::ext
    A0603["A0603 技术选型文档"]:::ext
    D105["D105 技术研讨纪要"]:::dat

    S0501["S0501 架构设计"]:::sop
    A0501["A0501 架构设计文档"]:::art
    S0502["S0502 架构决策"]:::sop
    A0502["A0502 架构决策记录"]:::art

    A0203 --> S0501
    A0301 --> S0501
    A0302 --> S0501
    A0303 --> S0501
    A0603 --> S0501
    S0501 --> A0501

    A0501 --> S0502
    A0603 --> S0502
    D105 --> S0502
    S0502 --> A0502

    A0502 --> S0501
```

### 非功能性设计

```mermaid
%%{init: {'flowchart': {'padding': 8, 'nodeSpacing': 32, 'rankSpacing': 32}} }%%
graph TD
    classDef sop fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E3A5F,rx:8,ry:8
    classDef art fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F

    A0501["A0501 架构设计文档"]:::art
    A0306["A0306 特性设计文档"]:::art

    S0503["S0503 容量设计"]:::sop
    A0503["A0503 容量规划方案"]:::art
    S0504["S0504 可用性设计"]:::sop
    A0504["A0504 高可用容错方案"]:::art
    S0505["S0505 安全设计"]:::sop
    A0505["A0505 安全防护方案"]:::art
    S0506["S0506 可观测性设计"]:::sop
    A0506["A0506 可观测性方案"]:::art

    A0501 --> S0503
    A0306 --> S0503
    S0503 --> A0503

    A0501 --> S0504
    A0306 --> S0504
    S0504 --> A0504

    A0501 --> S0505
    S0505 --> A0505

    A0501 --> S0506
    A0503 --> S0506
    A0504 --> S0506
    S0506 --> A0506
```

## SOP规范

| ID | Name | Description | Process |
| :--- | :--- | :--- | :--- |
| S0501 | 架构设计 | 确定系统边界与 C4 架构视图，建立产品级技术实现基线 | `{design-base}/process/sop-arch-design.md` |
| S0502 | 架构决策 | 评估技术方案选项，形成可追溯的架构决策记录 | `{design-base}/process/sop-adr.md` |
| S0503 | 容量设计 | 建立系统资源基线与 SLO，制定弹性扩容策略 | `{design-base}/process/sop-capacity-design.md` |
| S0504 | 可用性设计 | 定义 SLA/RTO/RPO 目标，设计熔断降级与故障恢复机制 | `{design-base}/process/sop-ha-design.md` |
| S0505 | 安全设计 | 识别系统安全威胁，制定认证鉴权与纵深防护方案 | `{design-base}/process/sop-security-design.md` |
| S0506 | 可观测性设计 | 构建系统可观测性体系，规范监控、日志与告警策略 | `{design-base}/process/sop-observability-design.md` |

## 外部输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| D105 | 技术研讨纪要 | 技术评审与讨论会议记录 | `references/tech-review-minutes/` |

## 上游输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| A0203 | 产品定义文档 | 产品定义文档，§9 NFR、§10 约束与依赖 | `concept/product-definition.md` |
| A0301 | 产品需求大纲 | 需求树与优先级，Theme/Epic/Feature 索引 | `requirements/requirements.md` |
| A0302 | 产品主题定义 | 业务主题与 Epic 拆分 | `requirements/<theme>/README.md` |
| A0303 | 产品史诗定义 | Epic 与 Feature 拆分 | `requirements/<theme>/<epic>/README.md` |
| A0603 | 技术选型文档 | 候选方案对比矩阵、加权评分决策、PoC 验证结果 | `technology/selections/<topic>.md` |
| A0306 | 特性设计文档 | 核心业务流程、数据约束与错误处理需求 | `requirements/<theme>/<epic>/<feature>/design.md` |

## 制品产出

| ID | Name | Description | File | Template |
| :--- | :--- | :--- | :--- | :--- |
| A0501 | 架构设计文档 | 产品级最高层技术文档，定义系统边界与模块职责，为各专项非功能设计提供统一基础 | `architecture/architecture.md` | `{design-base}/template/design/architecture.md` |
| A0502 | 架构决策记录 | 单项技术决策的正式存档，承载决策背景、备选方案与影响范围，支撑长期可追溯 | `architecture/adrs/adrNNN-<topic>.md` | `{design-base}/template/project/adr.md` |
| A0503 | 容量规划方案 | 系统运行容量基线文档，支撑资源采购、SLO 设定与弹性策略决策 | `architecture/capacity.md` | `{design-base}/template/design/capacity.md` |
| A0504 | 高可用容错方案 | 系统韧性保障蓝图，覆盖可用性目标、降级策略与故障恢复机制 | `architecture/high-availability.md` | `{design-base}/template/design/high-availability.md` |
| A0505 | 安全防护方案 | 系统安全基线文档，定义威胁边界、访问控制模型与合规审计要求 | `architecture/security.md` | `{design-base}/template/design/security.md` |
| A0506 | 可观测性方案 | 系统运行可见性蓝图，规范指标、日志与追踪标准，驱动告警与运维响应 | `architecture/observability.md` | `{design-base}/template/design/observability.md` |

## 新老编号对比

本阶段的SOP和制品产出重新编号，分别按照S05XX和A05XX，进行合理排序，并在做好新老编号对照表。

### SOP

| 新编号 | 旧编号 | 名称 |
| :--- | :--- | :--- |
| S0501 | S102 | 架构设计 |
| S0502 | S106 | 架构决策 |
| S0503 | S118 | 容量设计 |
| S0504 | S120 | 可用性设计 |
| S0505 | S121 | 安全设计 |
| S0506 | S122 | 可观测性设计 |

### 制品

| 新编号 | 旧编号 | 名称 |
| :--- | :--- | :--- |
| A0501 | A102 | 架构设计文档 |
| A0502 | A104 | 架构决策记录 |
| A0503 | A117 | 容量规划方案 |
| A0504 | A119 | 高可用容错方案 |
| A0505 | A120 | 安全防护方案 |
| A0506 | A121 | 可观测性方案 |

### 上游引用变更

| 旧引用 | 新引用 | 变更说明 |
| :--- | :--- | :--- |
| A106 逻辑流程 | A0306 特性设计文档 | 旧 A106/A107/A108（L2a Logic Design 产出）属于 P08 下游，不应反向作为 P05 输入；三行合并为 requirements/ 中的特性设计文档（A0306）作为设计约束来源 |
| A107 数据模型 | A0306 特性设计文档 | 同上 |
| A108 错误处理机制 | A0306 特性设计文档 | 同上 |

## 备注

- 将老的 A101 设计背景文档内容融入新的 A0501 架构设计文档，并清理重复章节与引用。
- 删除 原来S101，相关工作并入S0501，更新评审检查点与流程说明。
- A0501 架构设计文档须内嵌系统测试策略章节（测试金字塔、覆盖率目标、单元测试规范、测试数据管理、CI 质量门禁），不再单独产出测试策略文档（A1001 test-policy.md）。
