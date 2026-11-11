import collections
import json

from build_catalog import DIRECTIONS, ROOT, md, write


def main():
    papers = json.loads((ROOT / "catalog/papers.json").read_text(encoding="utf-8"))
    packages = json.loads((ROOT / "catalog/code_packages.json").read_text(encoding="utf-8"))
    lookup = {package["repository"]: package for package in packages}
    selected = [paper for paper in papers if paper["curated_note"]]
    lines = ["# 逐篇开源工作与可用性索引", "", "更新：2026-11-12。论文–仓库关联、源码归档、许可、数据与执行为不同状态。表中有些是相关工作、教程或组件，有些未找到许可证，不能把表的总行数称为可复现论文数。", "", "[研究路线](RESEARCH_ROADMAP.md) · [全部论文](ALL_PAPERS.md) · [全部包](../code_packages/README.md)", "", "## 统计口径", ""]
    counts = collections.Counter(paper["code"]["relationship"] for paper in selected)
    lines += ["| 对应关系 | DOI 去重篇数 |", "|---|---:|"]
    lines += [f"| `{name}` | {count} |" for name, count in sorted(counts.items())]
    collected = [paper for paper in selected if lookup[paper["code"]["repository"]]["collection_status"] in {"source_archive_collected", "partial_source_snapshot_collected"}]
    summary = {"date": "2026-11-12", "reviewed_paper_links": len(selected), "paper_relationship_counts": dict(counts), "papers_with_collected_source": len(collected), "papers_link_only_or_no_archive": len(selected) - len(collected), "unique_packages": len(packages), "strict_paper_reproductions": 0, "new_training_started_this_collection_stage": False}
    write("catalog/open_work_stats.json", json.dumps(summary, ensure_ascii=False, indent=2))
    lines += ["", f"已建立关联 {len(selected)} 篇；其中 {len(collected)} 篇的关联包已附完整或部分源码，其余 {len(selected) - len(collected)} 篇保留固定链接。完整包与部分包的数量仍以代码总索引为准。", ""]
    for category, direction in DIRECTIONS.items():
        subset = [paper for paper in selected if paper["category"] == category]
        if not subset:
            continue
        lines += ["## " + direction["name"], "", "| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |", "|---|---|---|---|---|"]
        for paper in subset:
            package = lookup[paper["code"]["repository"]]
            quartile = paper["jcr"]["reported_best_quartile"] or "?"
            lines.append(f"| {paper['year']} / [{paper['doi']}]({paper['doi_url']}) | [{md(paper['title'])}](../{paper['path']}/README.md) | {quartile}；官方年度待核 | [{md(package['repository'])}](../code_packages/{package['id']}/README.md)<br>{paper['code']['relationship']} | {package['collection_status']} |")
        for paper in subset:
            note = paper["curated_note"]
            lines += ["", "### " + paper["title"], "", "**研究问题：** " + note["problem"], "", "**实际入口：** " + note["entry"], "", "**依赖与数据：** " + note["dependencies"], "", "**当前边界：** " + note["limitations"]]
        lines.append("")
    lines += ["## 本轮未强行建立论文关联的线索", "", "- DENG-MIT/Inference_ConstV_EMs：README 明确要求邮件申请源码，不能把公开介绍页计为已收纳实现。", "- lz1025/AL-GA-combustion：README 的论文题名未匹配唯一 DOI，作为工具保留。", "- THGLab/H2Combustion_AL：燃烧主动学习源码可收纳，具体论文对应待核。", "- REALM、GBCT：预印本/开发中工作；数据与权重的承诺不等于已提供。", "- G-PARC、流场三维重建和热声制冷 COP：本轮查看后未确认直接燃烧研究，不放入燃烧核心论文列表。", "- 同一 ORCh/DFODE/CRNN 工具被多篇文章引用时，按关系类型逐篇说明，代码包只计一个。"]
    write("00_literature_map/OPEN_WORK_INDEX.md", "\n".join(lines))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
