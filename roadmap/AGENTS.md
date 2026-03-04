## 目录结构

路线图与交付节奏管理，包含版本规划、里程碑设计和迭代复盘。

```text
roadmap/
├── external/                   # 外部数据
│   ├── resource-capacity.md    #   资源容量
│   ├── customer-commitments.md #   客户承诺
│   ├── delivery-status/        #   交付状态 (实例级)
│   │   └── <topic>.md
│   └── team-feedback/          #   团队反馈 (实例级)
│       └── <topic>.md
├── README.md                   # 路线图
├── ms-<version>.md             # 里程碑计划
└── retro-<version>.md          # 迭代复盘报告
```

## 工作流程

```mermaid
%%{init: {'flowchart': {'padding': 8, 'nodeSpacing': 32, 'rankSpacing': 32}} }%%
graph TD
    classDef sop fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E3A5F,rx:8,ry:8
    classDef art fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F
    classDef dat fill:#F0FDF4,stroke:#16A34A,stroke-width:1.5px,color:#14532D

    A0203["A0203 产品定义文档"]:::art
    A0301["A0301 产品需求大纲"]:::art
    A0303["A0303 需求史诗定义"]:::art
    A0304["A0304 需求特性定义"]:::art
    D14["D14 资源容量"]:::dat
    D15["D15 客户承诺"]:::dat
    D16["D16 交付状态"]:::dat
    D17["D17 团队反馈"]:::dat

    S0401["S0401 路线图规划"]:::sop
    A0401["A0401 产品路线图"]:::art
    S0402["S0402 里程碑设计"]:::sop
    A0402["A0402 里程碑计划"]:::art
    S0403["S0403 迭代复盘"]:::sop
    A0403["A0403 迭代复盘报告"]:::art

    A0301 --> S0401
    A0203 --> S0401
    D14 --> S0401
    D15 --> S0401
    S0401 --> A0401

    A0401 --> S0402
    A0304 --> S0402
    A0303 --> S0402
    D16 --> S0402
    S0402 --> A0402

    A0402 --> S0403
    D17 --> S0403
    S0403 --> A0403
```

## SOP规范

| ID | Name | Description | Process |
| :--- | :--- | :--- | :--- |
| S0401 | 路线图规划 | 确定版本发布优先级与交付窗口，形成可承诺的产品路线图 | `{product-base}/process/sop-roadmap-plan.md` |
| S0402 | 里程碑设计 | 锁定版本关键交付节点，制定里程碑验收标准与风险管控策略 | `{product-base}/process/sop-roadmap-design.md` |
| S0403 | 迭代复盘 | 评审版本交付成果与流程效能，识别改进项并输入下轮规划 | `{product-base}/process/sop-retrospective.md` |

## 外部输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| D14 | 资源容量 | 团队资源与产能数据 | `external/resource-capacity.md` |
| D15 | 客户承诺 | 已签约客户交付承诺 | `external/customer-commitments.md` |
| D16 | 交付状态 | 当前迭代交付进度数据 | `external/delivery-status/` |
| D17 | 团队反馈 | 团队成员迭代反馈 | `external/team-feedback/` |

## 上游输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| A0203 | 产品定义文档 | 产品定义文档，明确范围与定位 | `concept/product-definition.md` |
| A0301 | 产品需求大纲 | 产品功能架构与需求主题目录 | `requirements/requirements.md` |
| A0303 | 产品史诗定义 | Epic 与 Feature 拆分 | `requirements/<theme>/<epic>/README.md` |
| A0304 | 需求特性定义 | 最小可交付功能单元定义 | `requirements/<theme>/<epic>/<feature>.md` |

## 制品产出

| ID | Name | Description | File | Template |
| :--- | :--- | :--- | :--- | :--- |
| A0401 | 路线图 | 产品版本序列与交付节奏全貌，各版本规划的决策主干 | `README.md` | `{product-base}/template/roadmap/rm-master.md` |
| A0402 | 里程碑计划 | 版本级交付承诺基准文档，锁定关键节点与验收准入，为周冲刺规划提供输入 | `ms-<version>.md` | `{product-base}/template/roadmap/rm-milestone.md` |
| A0403 | 迭代复盘报告 | 版本迭代成果与效能复盘存档，驱动路线图修订与团队改进 | `retro-<version>.md` | `{product-base}/template/roadmap/rm-retrospective.md` |

## 工作规则

- `{product-base}` 指 [it188-networkx/product-base](https://github.com/it188-networkx/product-base) 仓库，在当前 workspace 中对应子目录 `product-base/`。
- 建立或修改任意制品前，必须按以下顺序读取文件，缺一不可：
    1. 读取 **SOP 文件**：从 SOP规范 表格找到对应行的 Process 路径，用 read_file 读取全文，严格遵照其中的每一个步骤和指令执行。
    2. 读取 **制品模版文件**：从制品产出表格找到对应行的 Template 路径，用 read_file 读取全文，严格遵照模版中的结构、章节要求和注释指令生成内容。
    3. 两份文件中的指令若有冲突，以 SOP 文件为准。
