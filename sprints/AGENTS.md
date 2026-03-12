## 目录结构

冲刺执行空间，以 A2007 个人任务清单为核心，覆盖从批次规划、任务派发到状态自动同步的完整产品设计迭代闭环。

```text
sprints/
└── <YYYYMMDD>/                      # 周冲刺目录，以冲刺开始日期命名
    └── <user>-tasks/                #   A2007 个人任务清单（目录）
        ├── README.md                #     索引（元信息、状态总览）
        └── t{id}.md                 #     任务详情（每任务一个文件）
```

> - 冲刺目录 `<YYYYMMDD>` 以当周周一日期命名，例如 `20260303`。
> - `<user>` 为责任人英文缩写或 GitHub 用户名，与 `{ops-playbook}/team/skills.md` 中保持一致。

## 工作流程

```mermaid
graph LR
    classDef sop fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E3A5F,rx:8,ry:8
    classDef art fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F
    classDef ref fill:#F3F4F6,stroke:#6B7280,stroke-width:1.5px,color:#374151
    classDef wf fill:#D1FAE5,stroke:#059669,stroke-width:1.5px,color:#064E3B

    A2001["A2001 周冲刺计划"]:::ref
    S2011["S2011 冲刺初始化"]:::sop
    A2007["A2007 个人任务清单"]:::art
    S2012["S2012 冲刺规划"]:::sop
    S2013["S2013 冲刺执行"]:::sop

    A2001 --> S2011 -->|scaffold| A2007
    A2007 --> S2012 -->|已规划| A2007
    A2007 --> S2013 -->|可执行| A2007
```

## SOP 规范

| ID | Name | Description | Process | Issue Template |
| :--- | :--- | :--- | :--- | :--- |
| S2011 | 冲刺初始化 | 创建冲刺目录，从模板 scaffold A2007，从 A2001 提取冲刺目标写入 A2007，创建冲刺主 Issue | `{product-base}/process/sop-sprint-init.md` | [产品设计冲刺](../../.github/ISSUE_TEMPLATE/20-05-sprint-task-plan.yml) |
| S2012 | 冲刺规划 | 基于 A2001（init）或 A2007 状态总览表（supplement），拆解任务并标记「已规划」或「可执行」，更新 A2007 | `{product-base}/process/sop-sprint-plan.md` | — |
| S2013 | 冲刺执行 | 审查 A2007 中「已规划」任务的依赖就绪情况，升级为「可执行」或标记「阻塞中」 | `{product-base}/process/sop-sprint-exec.md` | — |

## 上游输入

| ID | Name | Source |
| :--- | :--- | :--- |
| A2001 | 周冲刺计划 | `{ops-playbook}/sprints/<YYYY>/plan<MMDD>.md` |

## 制品产出

| ID | Name | File | Template |
| :--- | :--- | :--- | :--- |
| A2007 | 个人任务清单 | `<YYYYMMDD>/<user>-tasks/README.md` | `{product-base}/template/sprint/sprint-tasks.md` |

## 工作规则

- `{ops-playbook}` 指 [it188-networkx/ops-playbook](https://github.com/it188-networkx/ops-playbook) 仓库，在当前 workspace 中对应子目录 `ops-playbook/`。
- `{product-base}` 指 [it188-networkx/product-base](https://github.com/it188-networkx/product-base) 仓库，在当前 workspace 中对应子目录 `product-base/`。
- 任务状态流转：已规划 → 可执行 → 已派发 → 待修订 → 已完成；另有「阻塞中」状态表示存在未解决的外部依赖。
- 建立或修改任意制品前，先读 SOP 文件全文，再读制品模板全文，冲突时以 SOP 为准。
- S2011 scaffold A2007 时只填写元信息和冲刺目标，其余章节保持空白模板状态。
- S2012 输出的规划须经人工确认后，方可提交变更触发 S2013 执行。
- S2012 init 模式以 A2001 为主输入；supplement 模式以 A2007 状态总览表为主输入。
- S2013 检查「已规划」任务的依赖关系，确认输入就绪后升级为「可执行」，或标记「阻塞中」。
- `sprint-task-dispatch.yml` 为「可执行」任务自动创建工单与 PR 并 assign 给 Copilot，状态更新为「已派发」。
- `sprint-task-status-sync.yml` 自动更新 A2007 状态：PR 合并标记「已完成」，PR 关闭未合并回退至「可执行」。
- 「阻塞中」与「已规划」不同：已规划是前置阶段未完成（内部依赖），阻塞中是存在未解决的外部依赖导致整个冲刺不可执行。
- 每批任务数量建议控制在 1-3 条，确保单批次可在一个工作日内完成审核闭环。

## SOP 注册表

| Key | Value |
| :--- | :--- |
| init-sop | `{product-base}/process/sop-sprint-init.md` |
| plan-sop | `{product-base}/process/sop-sprint-plan.md` |
| exec-sop | `{product-base}/process/sop-sprint-exec.md` |
