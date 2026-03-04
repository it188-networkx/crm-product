#!/usr/bin/env python3
"""
决策提取工具
从所有文档中提取关键决策记录，汇总到README
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime


def extract_decisions_from_file(file_path: Path) -> list:
    """从单个文件中提取决策记录"""
    decisions = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找决策表格
        # 匹配格式: | 日期 | 决策主题 | ... | 决策结论 | 决策人 |
        pattern = r'\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*\*\*选([^*]+)\*\*[^|]*\|\s*([^|]+?)\s*\|'
        matches = re.findall(pattern, content)

        for match in matches:
            date, topic, choice, person = match
            decisions.append({
                "date": date.strip(),
                "topic": topic.strip(),
                "choice": f"选{choice.strip()}",
                "person": person.strip(),
                "file": file_path.name
            })

        # 查找包含"决策"、"选择"关键词的章节
        decision_keywords = ["关键决策", "决策记录", "技术选型", "方案选择"]
        for keyword in decision_keywords:
            if keyword in content:
                # 简单标记该文件包含决策内容
                pass

    except Exception as e:
        print(f"警告: 读取文件失败 {file_path}: {e}")

    return decisions


def extract_all_decisions(project_path: str) -> list:
    """提取项目中所有决策记录"""
    project_root = Path(project_path)
    all_decisions = []

    print("=" * 60)
    print(f"扫描项目决策记录: {project_path}")
    print("=" * 60)
    print()

    # 扫描所有Markdown文件
    for file_path in project_root.rglob("*.md"):
        # 跳过README和模板文件
        if file_path.name == "README.md" or "template" in str(file_path):
            continue

        decisions = extract_decisions_from_file(file_path)
        if decisions:
            print(f"📄 {file_path.relative_to(project_root)}: 发现 {len(decisions)} 条决策")
            all_decisions.extend(decisions)

    return all_decisions


def generate_decision_report(project_path: str):
    """生成决策报告"""
    decisions = extract_all_decisions(project_path)

    if not decisions:
        print()
        print("⚠️  未发现决策记录")
        print("提示: 决策记录应包含以下格式的表格:")
        print("| 日期 | 决策主题 | 选项与权衡 | 最终结论 | 决策人 |")
        return

    # 按日期排序
    decisions.sort(key=lambda x: x["date"], reverse=True)

    print()
    print("=" * 60)
    print(f"共发现 {len(decisions)} 条决策记录")
    print("=" * 60)
    print()

    # 生成Markdown表格
    report = "## 🎯 关键决策记录\n\n"
    report += "| 日期 | 决策主题 | 决策结论 | 决策人 | 来源文档 |\n"
    report += "|------|---------|---------|--------|----------|\n"

    for decision in decisions:
        report += f"| {decision['date']} | {decision['topic']} | {decision['choice']} | {decision['person']} | {decision['file']} |\n"

    # 输出到控制台
    print(report)

    # 保存到文件
    output_path = Path(project_path) / "decisions-report.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# 决策记录报告\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(report)

    print()
    print(f"✅ 决策报告已保存: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python extract-decisions.py <项目路径>")
        print()
        print("示例:")
        print("  python extract-decisions.py ./my-product")
        sys.exit(1)

    project_path = sys.argv[1]

    if not Path(project_path).exists():
        print(f"❌ 项目路径不存在: {project_path}")
        sys.exit(1)

    generate_decision_report(project_path)


if __name__ == "__main__":
    main()
