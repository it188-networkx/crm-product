#!/usr/bin/env python3
"""
PRD统计工具
统计产品文档的规模和复杂度
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re


def count_lines(file_path: Path) -> int:
    """统计文件行数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception as e:
        print(f"警告: 无法读取文件 {file_path}: {e}")
        return 0


def count_words(file_path: Path) -> int:
    """统计文件字数（中英文）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 统计中文字符
            chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
            # 统计英文单词
            english_words = len(re.findall(r'\b[a-zA-Z]+\b', content))
            return chinese_chars + english_words
    except Exception as e:
        print(f"警告: 无法读取文件 {file_path}: {e}")
        return 0


def analyze_prd_structure(project_path: str) -> Dict:
    """分析PRD结构"""
    project_root = Path(project_path)
    planning_path = project_root / "planning"
    
    stats = {
        "master_prd": None,
        "epics": [],
        "features": [],
        "total_lines": 0,
        "total_words": 0
    }
    
    if not planning_path.exists():
        return stats
    
    # 查找Master PRD
    master_files = list(planning_path.glob("prd-master*.md"))
    if master_files:
        master_file = master_files[0]
        stats["master_prd"] = {
            "name": master_file.name,
            "lines": count_lines(master_file),
            "words": count_words(master_file)
        }
        stats["total_lines"] += stats["master_prd"]["lines"]
        stats["total_words"] += stats["master_prd"]["words"]
    
    # 查找Epic文档
    epic_files = list(planning_path.glob("epic-*.md"))
    for epic_file in epic_files:
        epic_stats = {
            "name": epic_file.name,
            "lines": count_lines(epic_file),
            "words": count_words(epic_file)
        }
        stats["epics"].append(epic_stats)
        stats["total_lines"] += epic_stats["lines"]
        stats["total_words"] += epic_stats["words"]
    
    # 查找Feature文档
    feature_files = list(planning_path.glob("feature-*.md"))
    for feature_file in feature_files:
        feature_stats = {
            "name": feature_file.name,
            "lines": count_lines(feature_file),
            "words": count_words(feature_file)
        }
        stats["features"].append(feature_stats)
        stats["total_lines"] += feature_stats["lines"]
        stats["total_words"] += feature_stats["words"]
    
    return stats


def analyze_all_documents(project_path: str) -> Dict:
    """分析所有文档"""
    project_root = Path(project_path)
    
    stage_stats = {}
    total_lines = 0
    total_words = 0
    total_files = 0
    
    stages = ["discovery", "concept", "planning", "design", "prototypes", 
              "commercialization", "growth"]
    
    for stage in stages:
        stage_path = project_root / stage
        if not stage_path.exists():
            continue
        
        stage_lines = 0
        stage_words = 0
        stage_files = 0
        
        for md_file in stage_path.rglob("*.md"):
            # 跳过templates目录
            if "templates" in md_file.parts:
                continue
            
            lines = count_lines(md_file)
            words = count_words(md_file)
            
            stage_lines += lines
            stage_words += words
            stage_files += 1
        
        if stage_files > 0:
            stage_stats[stage] = {
                "files": stage_files,
                "lines": stage_lines,
                "words": stage_words
            }
            total_lines += stage_lines
            total_words += stage_words
            total_files += stage_files
    
    return {
        "stages": stage_stats,
        "total_files": total_files,
        "total_lines": total_lines,
        "total_words": total_words
    }


def print_prd_report(project_path: str):
    """打印PRD统计报告"""
    print("=" * 60)
    print(f"PRD文档统计报告")
    print(f"项目路径: {project_path}")
    print("=" * 60)
    print()
    
    # PRD结构分析
    print("📊 PRD结构分析")
    print("-" * 60)
    prd_stats = analyze_prd_structure(project_path)
    
    if prd_stats["master_prd"]:
        master = prd_stats["master_prd"]
        print(f"Master PRD: {master['name']}")
        print(f"  - 行数: {master['lines']}")
        print(f"  - 字数: {master['words']}")
    else:
        print("⚠️  未找到Master PRD文档")
    
    print()
    print(f"Epic数量: {len(prd_stats['epics'])}")
    for i, epic in enumerate(prd_stats['epics'], 1):
        print(f"  {i}. {epic['name']}: {epic['lines']}行, {epic['words']}字")
    
    print()
    print(f"Feature数量: {len(prd_stats['features'])}")
    for i, feature in enumerate(prd_stats['features'], 1):
        print(f"  {i}. {feature['name']}: {feature['lines']}行, {feature['words']}字")
    
    print()
    print(f"PRD总计: {prd_stats['total_lines']}行, {prd_stats['total_words']}字")
    print()
    
    # 全文档分析
    print("📈 全文档统计")
    print("-" * 60)
    all_stats = analyze_all_documents(project_path)
    
    for stage, stats in all_stats["stages"].items():
        print(f"{stage}:")
        print(f"  - 文档数: {stats['files']}")
        print(f"  - 行数: {stats['lines']}")
        print(f"  - 字数: {stats['words']}")
    
    print()
    print("=" * 60)
    print(f"总计: {all_stats['total_files']}个文档, "
          f"{all_stats['total_lines']}行, {all_stats['total_words']}字")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        print("用法: python prd-stats.py <项目路径>")
        print("示例: python prd-stats.py /path/to/project")
        sys.exit(1)
    
    project_path = sys.argv[1]
    
    if not os.path.exists(project_path):
        print(f"错误: 项目路径不存在: {project_path}")
        sys.exit(1)
    
    print_prd_report(project_path)


if __name__ == "__main__":
    main()
