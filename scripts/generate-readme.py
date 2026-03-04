#!/usr/bin/env python3
"""
README生成工具
自动扫描项目目录，生成README导航表
"""

import os
import sys
from datetime import datetime
from pathlib import Path


def count_lines(file_path: Path) -> int:
    """统计文件行数"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except:
        return 0


def get_file_status(file_path: Path) -> str:
    """获取文件状态"""
    if not file_path.exists():
        return "⏳ 待完成"

    # 读取文件内容判断状态
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if 'status: "Draft"' in content or 'status: "待完成"' in content:
                return "🔄 进行中"
            elif 'status: "Approved"' in content or 'status: "已确认"' in content:
                return "✅ 已完成"
            else:
                return "🔄 进行中"
    except:
        return "🔄 进行中"


def get_last_modified(file_path: Path) -> str:
    """获取文件最后修改时间"""
    if not file_path.exists():
        return "-"

    timestamp = file_path.stat().st_mtime
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def scan_stage_docs(project_root: Path, stage: str, stage_name: str) -> list:
    """扫描指定阶段的文档"""
    stage_path = project_root / stage
    if not stage_path.exists():
        return []

    docs = []
    for file_path in sorted(stage_path.rglob("*.md")):
        # 跳过README
        if file_path.name == "README.md":
            continue

        rel_path = file_path.relative_to(project_root)
        docs.append(
            {
                "name": file_path.stem,
                "path": str(rel_path),
                "status": get_file_status(file_path),
                "lines": count_lines(file_path),
                "updated": get_last_modified(file_path),
            }
        )

    return docs


def generate_readme(project_path: str):
    """生成README文档"""
    project_root = Path(project_path)

    if not project_root.exists():
        print(f"❌ 项目路径不存在: {project_path}")
        sys.exit(1)

    print("=" * 60)
    print(f"扫描项目: {project_path}")
    print("=" * 60)
    print()

    # 扫描各阶段文档
    stages = [
        ("01-discovery", "需求发现 (Discovery)"),
        ("02-concept", "产品概念 (Concept)"),
        ("03-planning", "产品规划 (Planning)"),
        ("04-design", "产品设计 (Design)"),
        ("05-prototypes", "原型交付 (Prototypes)"),
        ("06-commercialization", "产品商业化 (Commercialization)"),
        ("07-growth", "产品增长 (Growth)"),
    ]

    readme_content = f"""# {{产品名称}} - 产品文档中心

> **项目概览**: {{一句话描述项目的核心目标和价值}}
> **当前版本**: v1.0
> **最后更新**: {datetime.now().strftime("%Y-%m-%d")}

## 📊 项目概览

| 属性 | 内容 |
|------|------|
| **产品名称** | {{产品名称}} |
| **产品版本** | v1.0 |
| **项目状态** | 规划中 |
| **产品负责人** | {{负责人姓名}} |
| **技术负责人** | {{技术负责人姓名}} |
| **目标发布日期** | {{发布日期}} |

---

## 📚 文档导航

"""

    for stage, stage_name in stages:
        docs = scan_stage_docs(project_root, stage, stage_name)

        if not docs:
            continue

        readme_content += f"### 阶段：{stage_name}\n\n"
        readme_content += "| 文档 | 状态 | 行数 | 最后更新 | 说明 |\n"
        readme_content += "|------|------|------|---------|------|\n"

        for doc in docs:
            readme_content += f"| [{doc['name']}](./{doc['path']}) | {doc['status']} | {doc['lines']} | {doc['updated']} | {{说明}} |\n"

        readme_content += "\n"

    readme_content += """**状态图例**:
- ✅ 已完成: 文档已完成并通过评审
- 🔄 进行中: 文档正在编写或修订中
- ⏳ 待完成: 文档尚未开始编写

---

## 🚀 快速链接

### 产品经理视角
- **核心文档**: [产品定义文档](./02-concept/product-definition.md) → [产品需求大纲](./03-planning/prd-master.md)
- **用户研究**: [用户研究](./01-discovery/user-research.md) → [需求分析](./01-discovery/requirement-analysis.md)

### 研发团队视角
- **需求文档**: [产品需求大纲](./03-planning/prd-master.md) → [Epic清单](./03-planning/)
- **技术设计**: [Tech设计](./04-design/)

---

**文档维护**: 本README由产品经理维护
**最后更新**: {datetime.now().strftime("%Y-%m-%d")}
"""

    # 写入README
    readme_path = project_root / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"✅ README生成完成: {readme_path}")
    print()
    print("=" * 60)
    print("提示: 请手动填充以下占位符:")
    print("  - {{产品名称}}")
    print("  - {{一句话描述项目的核心目标和价值}}")
    print("  - {{负责人姓名}}")
    print("  - {{技术负责人姓名}}")
    print("  - {{发布日期}}")
    print("  - 每个文档的{{说明}}")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python generate-readme.py <项目路径>")
        print()
        print("示例:")
        print("  python generate-readme.py ./my-product")
        sys.exit(1)

    project_path = sys.argv[1]
    generate_readme(project_path)


if __name__ == "__main__":
    main()
