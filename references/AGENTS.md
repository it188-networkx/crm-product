## 目录结构

存放外部原始数据与参考资料，按数据类型分类归档，为产品设计各类 SOP 提供上游输入。

```text
references/
├── industry-reports/           # D01 行业研报
│   └── <topic>.md
├── market-data/                # D02 市场数据
│   └── <topic>.md
├── competitor-materials/       # D04 竞品资料
│   └── <product>.md
├── surveys/                    # D05 问卷结果
│   └── <topic>.md
├── nps/                        # D07 NPS 数据
│   └── <topic>.md
├── customer-feedback/          # D08 客户反馈汇总
│   └── <topic>.md
├── bid-losses/                 # D09 竞标失分记录
│   └── <topic>.md
├── field-observations/         # D10 现场观察笔记
│   └── <topic>.md
├── strategy-docs/              # D11 企业经营战略
│   └── <topic>.md
├── team-assessments/           # D12 团队能力评估
│   └── <topic>.md
├── financial-data/             # D13 财务基准数据
│   └── <topic>.md
├── resource-capacity.md        # D14 资源容量
├── customer-commitments.md     # D15 客户承诺
├── delivery-status/            # D16 交付状态 (实例级)
│   └── <topic>.md
├── team-feedback/              # D17 团队反馈 (实例级)
│   └── <topic>.md
├── design-system-refs/         # D18 设计系统参考
│   └── <topic>.md
├── faq-tickets/                # D22 FAQ工单记录
│   └── <topic>.md
├── customer-implementations/   # D23 客户实施材料
│   └── <topic>.md
├── pricing/                    # D24 定价方案
│   └── <topic>.md
├── tracking/                   # D25 埋点数据
│   └── <topic>.md
├── ab-test/                    # D26 A/B 实验报告
│   └── <topic>.md
├── nps-csat/                   # D27 NPS/CSAT 调查
│   └── <topic>.md
├── retention/                  # D28 留存/付费数据
│   └── <topic>.md
├── sean-ellis/                 # D29 Sean Ellis 问卷
│   └── <topic>.md
├── external-requests/          # D30 外部需求
│   └── <topic>.md
├── external-feature-requests/  # D31 外部功能需求
│   └── <topic>.md
├── defect-sources/             # D32 外部缺陷来源
│   └── <topic>.md
├── solution-requests/          # D33 方案咨询要求
│   └── <topic>.md
├── config-requests/            # D35 产品配置要求
│   └── <topic>.md
├── demo-requests/              # D39 演示实施请求
│   └── <topic>.md
├── poc-results/                # D102 PoC 验证结果
│   └── <topic>.md
├── official-docs/              # D103 官方文档与社区资料
│   └── <topic>.md
└── tech-review-minutes/        # D105 技术研讨纪要
    └── <topic>.md
```

## 数据清单

| ID | Name | Description | Path |
| :--- | :--- | :--- | :--- |
| D01 | 行业研报 | 第三方行业研究报告 | `industry-reports/` |
| D02 | 市场数据 | 市场规模与趋势数据 | `market-data/` |
| D04 | 竞品资料 | 竞品产品公开资料与体验记录 | `competitor-materials/` |
| D05 | 问卷结果 | 用户调研问卷统计结果 | `surveys/` |
| D07 | NPS 数据 | 净推荐值调查数据 | `nps/` |
| D08 | 客户反馈汇总 | 多渠道客户反馈聚合 | `customer-feedback/` |
| D09 | 竞标失分记录 | 竞标过程中的失分项记录 | `bid-losses/` |
| D10 | 现场观察笔记 | 用户现场观察与记录 | `field-observations/` |
| D11 | 企业经营战略 | 企业级战略目标与业务方向文件 | `strategy-docs/` |
| D12 | 团队能力评估 | 研发与交付团队能力评估报告 | `team-assessments/` |
| D13 | 财务基准数据 | 产品投入产出财务基准数据 | `financial-data/` |
| D14 | 资源容量 | 团队资源与产能数据 | `resource-capacity.md` |
| D15 | 客户承诺 | 已签约客户交付承诺 | `customer-commitments.md` |
| D16 | 交付状态 | 当前迭代交付进度数据 | `delivery-status/` |
| D17 | 团队反馈 | 团队成员迭代反馈 | `team-feedback/` |
| D18 | 设计系统参考 | 外部设计系统规范与参考材料（如 Material Design、Ant Design 等） | `design-system-refs/` |
| D22 | FAQ工单记录 | 客服 FAQ 与工单记录 | `faq-tickets/` |
| D23 | 客户实施材料 | 客户侧实施过程材料 | `customer-implementations/` |
| D24 | 定价方案 | 产品定价策略与报价参考 | `pricing/` |
| D25 | 埋点数据 | 产品内用户行为埋点数据 | `tracking/` |
| D26 | A/B 实验报告 | A/B 测试实验结果 | `ab-test/` |
| D27 | NPS/CSAT 调查 | 满意度与推荐度调查数据 | `nps-csat/` |
| D28 | 留存/付费数据 | 用户留存率与付费转化数据 | `retention/` |
| D29 | Sean Ellis 问卷 | PMF 核心问卷调查结果 | `sean-ellis/` |
| D30 | 外部需求 | 来自外部渠道的需求输入 | `external-requests/` |
| D31 | 外部功能需求 | 来自销售/客户渠道的功能需求汇总 | `external-feature-requests/` |
| D32 | 外部缺陷来源 | 来自客户/监控的缺陷反馈原始数据 | `defect-sources/` |
| D33 | 方案咨询要求 | 客户提出的售前方案咨询需求 | `solution-requests/` |
| D35 | 产品配置要求 | 客户提出的产品配置需求 | `config-requests/` |
| D39 | 演示实施请求 | 客户或内部提出的演示请求 | `demo-requests/` |
| D102 | PoC 验证结果 | 概念验证的测试结论与 Benchmark 报告 | `poc-results/` |
| D103 | 官方文档与社区资料 | 官方文档、版本公告与社区实践材料 | `official-docs/` |
| D105 | 技术研讨纪要 | 技术评审与讨论会议记录 | `tech-review-minutes/` |
