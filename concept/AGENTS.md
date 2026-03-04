## 目录结构

产品级文档，记录从概念到定义的演进。

```text
concept/
├── product-concept.md          # 产品概念书
├── business-requirement.md     # 商业需求文档 (商业需求文档)
└── product-definition.md       # 产品定义文档 (产品定义文档)
```

## 工作流程

```mermaid
%%{init: {'flowchart': {'padding': 8, 'nodeSpacing': 32, 'rankSpacing': 32}} }%%
graph TD
    classDef sop fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E3A5F,rx:8,ry:8
    classDef art fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F
    classDef dat fill:#F0FDF4,stroke:#16A34A,stroke-width:1.5px,color:#14532D

    A0101["A0101 市场调研报告"]:::art
    A0102["A0102 竞争分析报告"]:::art
    A0103["A0103 用户画像文档"]:::art
    A0106["A0106 需求分析报告"]:::art
    D11["D11 企业经营战略"]:::dat
    D12["D12 团队能力评估"]:::dat
    D13["D13 财务基准数据"]:::dat

    S0201["S0201 产品构思"]:::sop
    A0201["A0201 产品概念书"]:::art
    S0202["S0202 商业论证"]:::sop
    A0202["A0202 商业需求文档"]:::art
    S0203["S0203 产品定义"]:::sop
    A0203["A0203 产品定义文档"]:::art

    D11 --> S0201
    D12 --> S0201
    S0201 --> A0201

    A0201 --> S0202
    A0101 --> S0202
    A0102 --> S0202
    D13 --> S0202
    S0202 --> A0202

    A0201 --> S0203
    A0202 --> S0203
    A0103 --> S0203
    A0106 --> S0203
    S0203 --> A0203
```

## SOP规范

| ID | Name | Description | Process |
| :--- | :--- | :--- | :--- |
| S0201 | 产品构思 | 结合企业战略与团队能力，确立产品核心方向与初步假设 | `{product-base}/process/sop-product-concept.md` |
| S0202 | 商业论证 | 评估市场机会与商业可行性，形成产品立项投资决策依据 | `{product-base}/process/sop-business-requirement.md` |
| S0203 | 产品定义 | 锁定产品定位、边界与核心功能范围，建立研发立项基准 | `{product-base}/process/sop-product-definition.md` |

## 外部输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| D11 | 企业经营战略 | 公司战略方向与经营目标 | `{product-base}/references/business-strategy.md` |
| D12 | 团队能力评估 | 团队技术和业务能力现状 | `{product-base}/references/team-capability.md` |
| D13 | 财务基准数据 | 成本、收入等财务基准 | `{product-base}/references/financial-baseline.md` |

## 上游输入

| ID | Name | Description | Source |
| :--- | :--- | :--- | :--- |
| A0101 | 市场调研报告 | 市场调研结论与洞察 | `discovery/market/` |
| A0102 | 竞争分析报告 | 竞品对标分析结论 | `discovery/competitors/` |
| A0103 | 用户画像文档 | 用户研究发现与画像 | `discovery/users/` |
| A0106 | 需求分析报告 | 结构化需求与商业价值评估 | `discovery/requirements/` |

## 制品产出

| ID | Name | Description | File | Template |
| :--- | :--- | :--- | :--- | :--- |
| A0201 | 产品概念书 | 概念阶段首份产品文件，记录核心方向与战略假设 | `product-concept.md` | `{product-base}/template/concept/product-concept.md` |
| A0202 | 商业需求文档 | 论证商业可行性与市场机会，为立项投资决策提供依据 | `business-requirement.md` | `{product-base}/template/concept/business-requirement.md` |
| A0203 | 产品定义文档 | 明确产品定位、边界与核心功能范围，作为需求与设计的输入基准 | `product-definition.md` | `{product-base}/template/concept/product-definition.md` |

## 新老编号对比

本阶段的SOP和制品产出重新编号，分别按照S02XX和A02XX，进行合理排序，并在做好新老编号对照表。

### SOP

| 新编号 | 旧编号 | 名称 |
| :--- | :--- | :--- |
| S0201 | S05 | 产品构思 |
| S0202 | S06 | 商业论证 |
| S0203 | S07 | 产品定义 |

### 制品

| 新编号 | 旧编号 | 名称 |
| :--- | :--- | :--- |
| A0201 | A05 | 产品概念书 |
| A0202 | A06 | 商业需求文档 |
| A0203 | A07 | 产品定义文档 |

## 备注

- 文档路径中的 `{product-base}` 指 [it188-networkx/product-base](https://github.com/it188-networkx/product-base) 仓库，
  通常作为独立子目录位于当前 workspace 根目录下。
