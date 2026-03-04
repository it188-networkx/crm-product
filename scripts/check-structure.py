#!/usr/bin/env python3
"""
产品文档结构检查工具
检查产品文档目录结构的完整性和规范性
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# 定义7阶段标准结构
STANDARD_STRUCTURE = {
    "discovery": {
        "required": True,
        "templates": [
            "competitive-analysis.md",
            "market-research.md",
            "requirement-analysis.md",
            "requirement-matching.md",
            "user-research.md",
        ],
    },
    "concept": {"required": True, "templates": ["product-definition.md"]},
    "planning": {"required": True, "templates": ["prd-master-template.md", "epic-template.md", "feature-template.md"]},
    "design": {"required": True, "templates": ["ux-design.md", "tech-design.md"]},
    "prototypes": {"required": False, "templates": []},
    "commercialization": {"required": True, "templates": ["release-notes.md", "user-manual.md"]},
    "growth": {"required": False, "templates": []},
}


def check_directory_structure(project_path: str) -> Tuple[bool, List[str]]:
    """检查目录结构"""
    issues = []
    project_root = Path(project_path)

    if not project_root.exists():
        return False, [f"项目路径不存在: {project_path}"]

    # 检查7个阶段目录
    for stage, config in STANDARD_STRUCTURE.items():
        stage_path = project_root / stage

        if not stage_path.exists():
            if config["required"]:
                issues.append(f"❌ 缺少必需目录: {stage}/")
            else:
                issues.append(f"⚠️  缺少可选目录: {stage}/")
        else:
            # 检查templates子目录
            templates_path = stage_path / "templates"
            if config["templates"] and not templates_path.exists():
                issues.append(f"⚠️  {stage}/ 目录下缺少 template/ 子目录")

    return len(issues) == 0, issues


def check_document_completeness(project_path: str) -> Tuple[bool, List[str]]:
    """检查文档完整性"""
    issues = []
    project_root = Path(project_path)

    # 检查必需文档
    required_docs = [
        ("README.md", "项目根目录"),
        ("discovery/requirement-analysis.md", "需求分析文档"),
        ("concept/product-definition.md", "产品定义文档"),
        ("planning/prd-master.md", "Master PRD文档"),
    ]

    for doc_path, doc_name in required_docs:
        full_path = project_root / doc_path
        if not full_path.exists():
            issues.append(f"❌ 缺少必需文档: {doc_name} ({doc_path})")

    # 检查设计阶段文档
    design_path = project_root / "design"

    return len(issues) == 0, issues


def check_ai_instructions(project_path: str) -> Tuple[bool, List[str]]:
    """检查模板是否包含AI生成指令"""
    issues = []
    project_root = Path(project_path)

    # 检查关键模板文件
    template_files = [
        "planning/template/epic-template.md",
        "planning/template/feature-template.md",
        "concept/template/pdd-template.md",
        "design/template/ux-design-template.md",
    ]

    for template_path in template_files:
        full_path = project_root / template_path
        if full_path.exists():
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "<!-- [指令] -->" not in content and "<!--\n[指令]" not in content:
                        issues.append(f"⚠️  模板缺少AI生成指令: {template_path}")
            except:
                pass

    return len(issues) == 0, issues


def check_naming_convention(project_path: str) -> Tuple[bool, List[str]]:
    """检查命名规范"""
    issues = []
    project_root = Path(project_path)

    # 检查目录名是否有数字前缀
    for item in project_root.iterdir():
        if item.is_dir() and item.name[0].isdigit():
            issues.append(f"⚠️  目录名包含数字前缀: {item.name}")

    # 检查文档名是否规范（小写+连字符）
    for stage in STANDARD_STRUCTURE.keys():
        stage_path = project_root / stage
        if stage_path.exists():
            for doc in stage_path.rglob("*.md"):
                if doc.name != doc.name.lower():
                    issues.append(f"⚠️  文档名应使用小写: {doc.relative_to(project_root)}")

    return len(issues) == 0, issues


def print_report(project_path: str):
    """打印检查报告"""
    print("=" * 60)
    print(f"产品文档结构检查报告")
    print(f"项目路径: {project_path}")
    print("=" * 60)
    print()

    # 检查目录结构
    print("📁 目录结构检查")
    print("-" * 60)
    structure_ok, structure_issues = check_directory_structure(project_path)
    if structure_ok:
        print("✅ 目录结构完整")
    else:
        for issue in structure_issues:
            print(f"  {issue}")
    print()

    # 检查文档完整性
    print("📄 文档完整性检查")
    print("-" * 60)
    docs_ok, docs_issues = check_document_completeness(project_path)
    if docs_ok:
        print("✅ 必需文档齐全")
    else:
        for issue in docs_issues:
            print(f"  {issue}")
    print()

    # 检查命名规范
    print("📝 命名规范检查")
    print("-" * 60)
    naming_ok, naming_issues = check_naming_convention(project_path)
    if naming_ok:
        print("✅ 命名规范符合要求")
    else:
        for issue in naming_issues:
            print(f"  {issue}")
    print()

    # 检查AI生成指令
    print("🤖 AI生成指令检查")
    print("-" * 60)
    ai_ok, ai_issues = check_ai_instructions(project_path)
    if ai_ok:
        print("✅ 模板包含AI生成指令")
    else:
        for issue in ai_issues:
            print(f"  {issue}")
    print()

    # 总结
    print("=" * 60)
    all_ok = structure_ok and docs_ok and naming_ok and ai_ok
    if all_ok:
        print("✅ 检查通过！文档结构完整且规范")
        return 0
    else:
        total_issues = len(structure_issues) + len(docs_issues) + len(naming_issues)
        print(f"⚠️  发现 {total_issues} 个问题，请修复后重新检查")
        return 1


def main():
    if len(sys.argv) < 2:
        print("用法: python check-structure.py <项目路径>")
        print("示例: python check-structure.py /path/to/project")
        sys.exit(1)

    project_path = sys.argv[1]
    exit_code = print_report(project_path)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
