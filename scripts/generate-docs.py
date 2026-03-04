#!/usr/bin/env python3
"""
文档生成工具
从模板快速生成产品文档骨架
"""

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

TEMPLATES = {
    "discovery": [
        "competitive-analysis.md",
        "market-research.md",
        "requirement-analysis.md",
        "requirement-matching.md",
        "user-research.md"
    ],
    "concept": ["product-definition.md"],
    "planning": [
        "prd-master.md",
        "epic-{name}.md",
        "feature-{name}.md"
    ],
    "design": ["ux-design.md", "tech-design.md"],
    "commercialization": ["release-notes.md", "user-manual.md"]
}


def generate_stage_docs(template_root: Path, target_root: Path, stage: str,
                       product_name: str = "产品名称"):
    """生成指定阶段的文档"""
    template_stage = template_root / stage / "templates"
    target_stage = target_root / stage

    if not template_stage.exists():
        print(f"⚠️  模板目录不存在: {template_stage}")
        return

    # 创建目标目录
    target_stage.mkdir(parents=True, exist_ok=True)

    # 复制模板文件
    templates = TEMPLATES.get(stage, [])
    for template_name in templates:
        # 跳过带占位符的模板
        if "{name}" in template_name:
            continue

        template_file = template_stage / template_name
        if template_file.exists():
            target_file = target_stage / template_name
            shutil.copy2(template_file, target_file)

            # 替换占位符
            replace_placeholders(target_file, product_name)
            print(f"✅ 生成: {stage}/{template_name}")


def replace_placeholders(file_path: Path, product_name: str):
    """替换文档中的占位符"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 替换常见占位符
        replacements = {
            "[产品名称]": product_name,
            "[版本号]": "v1.0",
            "[姓名]": os.getenv("USER", "产品经理"),
            "YYYY-MM-DD": datetime.now().strftime("%Y-%m-%d")
        }

        for old, new in replacements.items():
            content = content.replace(old, new)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"警告: 替换占位符失败 {file_path}: {e}")


def generate_epic(template_root: Path, target_root: Path, epic_name: str,
                 product_name: str = "产品名称"):
    """生成Epic文档"""
    template_file = template_root / "planning" / "templates" / "epic-template.md"
    target_file = target_root / "planning" / f"epic-{epic_name}.md"

    if not template_file.exists():
        print(f"❌ Epic模板不存在: {template_file}")
        return

    # 创建目标目录
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # 复制并替换
    shutil.copy2(template_file, target_file)

    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace("[Epic名称]", epic_name)
        content = content.replace("[产品名称]", product_name)
        content = content.replace("YYYY-MM-DD", datetime.now().strftime("%Y-%m-%d"))

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 生成Epic: planning/epic-{epic_name}.md")
    except Exception as e:
        print(f"❌ 生成Epic失败: {e}")


def generate_feature(template_root: Path, target_root: Path, feature_name: str,
                    epic_name: str = "Epic名称"):
    """生成Feature文档"""
    template_file = template_root / "planning" / "templates" / "feature-template.md"
    target_file = target_root / "planning" / f"feature-{feature_name}.md"

    if not template_file.exists():
        print(f"❌ Feature模板不存在: {template_file}")
        return

    # 创建目标目录
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # 复制并替换
    shutil.copy2(template_file, target_file)

    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace("[Feature名称]", feature_name)
        content = content.replace("[Epic名称]", epic_name)
        content = content.replace("YYYY-MM-DD", datetime.now().strftime("%Y-%m-%d"))

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 生成Feature: planning/feature-{feature_name}.md")
    except Exception as e:
        print(f"❌ 生成Feature失败: {e}")


def generate_project(template_root: Path, target_path: str, product_name: str):
    """生成完整项目结构"""
    target_root = Path(target_path)

    print("=" * 60)
    print(f"生成产品文档结构: {product_name}")
    print(f"目标路径: {target_path}")
    print("=" * 60)
    print()

    # 创建项目根目录
    target_root.mkdir(parents=True, exist_ok=True)

    # 生成各阶段文档
    stages = ["discovery", "concept", "planning", "design", "commercialization"]
    for stage in stages:
        print(f"📁 生成 {stage} 阶段文档...")
        generate_stage_docs(template_root, target_root, stage, product_name)

    # 创建空目录
    (target_root / "prototypes").mkdir(exist_ok=True)
    (target_root / "growth").mkdir(exist_ok=True)

    # 复制README
    template_readme = template_root / "README.md"
    if template_readme.exists():
        target_readme = target_root / "README.md"
        shutil.copy2(template_readme, target_readme)
        replace_placeholders(target_readme, product_name)
        print(f"✅ 生成: README.md")

    print()
    print("=" * 60)
    print("✅ 项目结构生成完成！")
    print("=" * 60)


def generate_readme(template_root: Path, target_path: str):
    """生成README文档"""
    template_file = template_root / "README-template.md"
    target_file = Path(target_path) / "README.md"

    if not template_file.exists():
        print(f"❌ README模板不存在: {template_file}")
        return

    # 复制模板
    shutil.copy2(template_file, target_file)
    print(f"✅ 生成README: {target_file}")


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  生成完整项目:      python generate-docs.py project <目标路径> <产品名称>")
        print("  生成Epic:          python generate-docs.py epic <Epic名称> [产品名称]")
        print("  生成Feature:       python generate-docs.py feature <Feature名称> [Epic名称]")
        print("  生成README:        python generate-docs.py readme <目标路径>")
        print()
        print("示例:")
        print("  python generate-docs.py project ./my-product 智能告警系统")
        print("  python generate-docs.py epic 告警分析 智能告警系统")
        print("  python generate-docs.py feature 根因分析 告警分析")
        print("  python generate-docs.py readme ./my-product")
        sys.exit(1)

    # 获取模板根目录（脚本所在目录的上级目录）
    script_dir = Path(__file__).parent
    template_root = script_dir.parent

    command = sys.argv[1]

    if command == "project":
        if len(sys.argv) < 4:
            print("错误: 缺少参数")
            print("用法: python generate-docs.py project <目标路径> <产品名称>")
            sys.exit(1)

        target_path = sys.argv[2]
        product_name = sys.argv[3]
        generate_project(template_root, target_path, product_name)

    elif command == "epic":
        if len(sys.argv) < 3:
            print("错误: 缺少Epic名称")
            sys.exit(1)

        epic_name = sys.argv[2]
        product_name = sys.argv[3] if len(sys.argv) > 3 else "产品名称"
        target_root = Path.cwd()
        generate_epic(template_root, target_root, epic_name, product_name)

    elif command == "feature":
        if len(sys.argv) < 3:
            print("错误: 缺少Feature名称")
            sys.exit(1)

        feature_name = sys.argv[2]
        epic_name = sys.argv[3] if len(sys.argv) > 3 else "Epic名称"
        target_root = Path.cwd()
        generate_feature(template_root, target_root, feature_name, epic_name)

    elif command == "readme":
        if len(sys.argv) < 3:
            print("错误: 缺少目标路径")
            print("用法: python generate-docs.py readme <目标路径>")
            sys.exit(1)

        target_path = sys.argv[2]
        generate_readme(template_root, target_path)

    else:
        print(f"错误: 未知命令 '{command}'")
        print("支持的命令: project, epic, feature, readme")
        sys.exit(1)


if __name__ == "__main__":
    main()
