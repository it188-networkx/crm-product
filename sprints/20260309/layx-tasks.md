# 周冲刺任务

- 迭代周期：2026-03-09 ~ 2026-03-14
- 责任人：赖毅
- 周冲刺计划：`{ops-playbook}/sprints/20260309/sprint-plan.md`
- 更新时间：2026-03-10 10:00

## 待澄清问题 (Open Questions)

| 问题ID | 涉及任务 | 问题描述 | 期望获取的信息/文档 | 提出时间 |
| :--- | :--- | :--- | :--- | :--- |
| Q001 | 101202 | CRM 为新产品，`discovery/` 目录下尚无需求分析报告（A0106），S0302 功能主题规划的上游输入 A0106 缺失——本迭代是否基于 A0203 产品定义文档中已有的 MVP 范围直接推导 Theme 划分，还是需要先补齐需求分析？ | 若直接推导，请确认 A0203 Section 1.4 MVP 范围可作为 Theme 划分的充分输入；若需补齐，需追加 S0106 需求分析任务并调整排期 | 03-10 |
| Q002 | 101202 | 本迭代产品需求输出的深度——仅推进至 S0302 功能主题规划（A0302），还是需进一步推进至 S0303 功能史诗规划（A0303）？当前 1-2 天周容量在完成 S0301 + S0302 后已接近上限，若需 S0303 则需延至下一迭代或调整容量 | 请确认本迭代需求输出的目标 SOP 层级 | 03-10 |

## 状态总览 (Status Overview)

| 任务编号 | 任务描述 | 关联工单 | 预计完成 | 实际完成 | 工作量 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101201 | S0301 功能架构规划：编制 CRM 产品需求大纲（A0301） | | 03-12 | | 1 天 | 已规划 |
| 101202 | S0302 功能主题规划：编制 CRM 首批需求主题定义（A0302） | | 03-14 | | 1 天 | 已规划 |

## 冲刺任务 (Sprint Tasks)

### 101201 S0301 功能架构规划：编制 CRM 产品需求大纲

**任务概要**

- 目标：按 S0301 功能架构规划 SOP，基于已有产品定义文档（A0203）编制 CRM 产品需求大纲（A0301），建立 Theme / Epic / Feature 三级需求结构索引，锁定 MVP 功能范围与核心功能定义，为后续 S0302 功能主题规划提供顶层框架输入
- 关联工单：
- 关联 PR：
- 预计完成：03-12
- 实际完成：
- 工作量估算：1 天
- 状态：已规划

---

**上下文**

- 产品定义文档（A0203）：`concept/product-definition.md`（草稿状态），Section 1.4 MVP 包含范围定义了 4 大功能域（AI 增效工作流、结构化销售闭环、知识沉淀体系、老板决策看板）；Section 1.5 里程碑定义了 M1-M12 交付节奏
- 商业需求文档（A0202）：`concept/business-requirement.md`（草稿状态），Section 2 内部效率目标提供 M1/M3/M6/M12 验收指标
- 产品概念书（A0201）：`concept/product-concept.md`（草稿状态），Section 6 初步范围
- 需求分析报告（A0106）：`discovery/requirements/` — 目录不存在，本迭代基于 A0203 直接推导
- 需求变更记录（A0305）：无（新产品无历史变更）
- 需求目录规范：`requirements/AGENTS.md`（design-variant = lowcode）
- 功能架构规划 SOP（S0301）：`{product-base}/process/sop-prd-master.md`
- 功能架构规划工单模版：`.github/ISSUE_TEMPLATE/P03-01-prd-master.yml`
- 上游制品：`{ops-playbook}/sprints/20260309/sprint-plan.md` 第 1012 行
- 过程参考：`{ops-playbook}/sops/workflow/product-design.md`（W301 产品需求规划章节）

**处理规程**

SOP：`{product-base}/process/sop-prd-master.md`（S0301 功能架构规划）
工单模版：`.github/ISSUE_TEMPLATE/P03-01-prd-master.yml`

**预期制品**

- 制品：`requirements/requirements.md`（A0301 产品需求大纲），包含 MVP 功能范围确认、Theme / Epic / Feature 三级层次索引与各 Theme 简要定义
- 模板：`{product-base}/template/requirements/requirements.md`

---

### 101202 S0302 功能主题规划：编制 CRM 首批需求主题定义

**任务概要**

- 目标：按 S0302 功能主题规划 SOP，基于 101201 产出的产品需求大纲（A0301），为 MVP 范围内的首批 Theme 编制需求主题定义（A0302），按价值流组织业务主题并建立 Epic 拆分索引，为后续迭代的 S0303 功能史诗规划提供输入
- 关联工单：
- 关联 PR：
- 预计完成：03-14
- 实际完成：
- 工作量估算：1 天
- 状态：已规划

---

**上下文**

- 产品需求大纲（A0301）：`requirements/requirements.md` — 101201 产出，提供 Theme 列表与功能架构索引
- 产品定义文档（A0203）：`concept/product-definition.md`，Section 3 目标用户（用户角色与价值流映射）、Section 4 商业逻辑（各角色价值主张）
- 需求分析报告（A0106）：缺失（见 Q001）
- 需求变更记录（A0305）：无
- 需求目录规范：`requirements/AGENTS.md`（design-variant = lowcode）
- 功能主题规划 SOP（S0302）：`{product-base}/process/sop-prd-theme.md`
- 功能主题规划工单模版：`.github/ISSUE_TEMPLATE/P03-02-prd-theme.yml`
- 上游制品：101201 → A0301
- 过程参考：`{ops-playbook}/sops/workflow/product-design.md`（W301 产品需求规划章节）

**处理规程**

SOP：`{product-base}/process/sop-prd-theme.md`（S0302 功能主题规划）
工单模版：`.github/ISSUE_TEMPLATE/P03-02-prd-theme.yml`

**预期制品**

- 制品：`requirements/<theme>/README.md`（A0302 需求主题定义），每个 Theme 一个目录，Theme README 包含业务主题定义、价值流归属与 Epic 拆分索引
- 模板：`{product-base}/template/requirements/theme.md`

## 自检清单

- [ ] A2002 文件存在于 `crm-product/sprints/20260309/layx-tasks.md`
- [ ] 任务清单覆盖 A2001 中分配给本人的全部交付目标（1012）
- [ ] 每项任务有唯一任务 ID（101201、101202）并包含四要素（任务目标/上下文/处理规程/预期制品）
- [ ] 每项任务对齐 W301 产品设计流程中的具体 SOP（S0301、S0302）
- [ ] 任务粒度符合标准（0.5 天至 2 天）
- [ ] 待澄清问题区块已登记所有 AI 识别到的信息缺口（Q001、Q002）
- [ ] 已将 A2002 路径回写至 A2001 "个人冲刺任务"区块
- [ ] 有疑问或无法承接的任务已在备注标注 `[待确认]` 并告知敏捷教练
