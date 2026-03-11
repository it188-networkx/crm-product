## 目录结构

冲刺执行空间，承载 S2005 冲刺任务规划产出的个人冲刺任务清单（A2002）。

```text
sprints/
└── <YYYYMMDD>/                      # 周冲刺目录，以冲刺开始日期命名
    └── <user>-tasks.md              #   A2002 个人冲刺任务清单
```

> - 冲刺目录 `<YYYYMMDD>` 以当周周一日期命名，例如 `20260303`。
> - `<user>` 为责任人英文缩写或 GitHub 用户名，与 `{ops-playbook}/team/skills.md` 中保持一致。

## SOP 规范

| ID | Name | Description | Process |
| :--- | :--- | :--- | :--- |
| S2005 | 冲刺任务规划 | 锁定各责任人本周执行任务，建立个人交付基线 | `{ops-playbook}/process/agile-dev/sop-sprint-task-plan-product.md` |

## 上游输入

| ID | Name | Source |
| :--- | :--- | :--- |
| A2001 | 周冲刺计划 | `{ops-playbook}/sprints/<YYYYMMDD>/sprint-plan.md` |

## 制品产出

| ID | Name | File | Template |
| :--- | :--- | :--- | :--- |
| A2002 | 周冲刺任务 | `<YYYYMMDD>/<user>-tasks.md` | `{ops-playbook}/template/sprint-tasks.md` |

## 工作规则

- `{ops-playbook}` 指 [it188-networkx/ops-playbook](https://github.com/it188-networkx/ops-playbook) 仓库，在当前 workspace 中对应子目录 `ops-playbook/`。
- 建立或修改任意制品前，必须按以下顺序读取文件，缺一不可：
    1. 读取 **SOP 文件**：从 SOP 规范表格找到对应行的 Process 路径，用 read_file 读取全文，严格遵照其中的每一个步骤和指令执行。
    2. 读取 **制品模版文件**：从制品产出表格找到对应行的 Template 路径，用 read_file 读取全文，严格遵照模版中的结构、章节要求和注释指令生成内容。
    3. 两份文件中的指令若有冲突，以 SOP 文件为准。
