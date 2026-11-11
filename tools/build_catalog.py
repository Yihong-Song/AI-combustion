import collections
import csv
import hashlib
import html
import json
import pathlib
import re
import shutil

from direction_content import DIRECTIONS


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATE = "2026-11-12"
STATUS = {
    "provisional_q1_q2": "二级来源报告 Q1/Q2，JCR 版本待官方核实",
    "pending_jcr": "JCR 分区待核实",
    "adjacent_q3_q4": "二级来源报告 Q3/Q4，不纳入 Q1/Q2 候选主集"
}
SUPPORT = {
    "DENG-MIT/CRNN": "通用化学反应网络发现及 Bayesian cathode 子项目；不同子项目环境不同。",
    "DENG-MIT/CRNN-Pyrolysis": "热解 CRNN 补充实现；与 Biomass.jl 的论文关系需逐项核实。",
    "DENG-MIT/Arrhenius.jl": "Julia 可微化学计算工具；用于机理参数校准的基础设施。",
    "DENG-MIT/Arrhenius_Flame_1D": "可微一维火焰工具，具体论文对应关系待核实。",
    "DENG-MIT/ArrheniusOpt": "机理参数优化工具；未定位许可，链接收纳。",
    "DENG-MIT/reactorch": "PyTorch 热化学模块，结合 Cantera 机理；属于可微计算基础设施。",
    "DENG-MIT/StiffNeuralODE": "刚性 Neural ODE 通用方法；Robertson/Pollution 等测试不等同真实燃烧验证。",
    "DENG-MIT/Stiff-PINN": "刚性 PINN/QSSA 基准，非整套详细火焰复现；未定位许可。",
    "DENG-MIT/DeepReduction": "神经 ODE 化学缩减线索，README 对应预印本/会议，不能预设 JCR。",
    "DENG-MIT/CRNN_HyChem": "CRNN 与 HyChem 初步探索，不能当作已核实期刊实现。",
    "DENG-MIT/ChemKAN": "KAN 化学模型新方法线索；固定提交无根 README/许可，论文关系待核实。",
    "DENG-MIT/CoFFe": "稀疏多模态场重建与算子解码工具，论文对应与燃烧范围待核实。",
    "deepflameCFD/deepflame-dev": "OpenFOAM/Cantera/LibTorch 反应流框架；README 的部分 DNN 权重需向作者申请，不能保证直接运行。",
    "caic99/deepflame-kit": "DeepFlame 配套工具；需检查与主框架提交、机理和网络格式是否匹配。",
    "burn-research/Cypher-challenge-2025": "LES 亚格子扩散建模竞赛基准，a priori 结果不等于后验稳定性。",
    "samuelburbulla/FLAME-AI": "流动超分辨率挑战；名称含 FLAME 不足以证明所有算例为反应流。作为相邻数据方法。",
    "jiweiqi/CombustionNet": "燃烧数据资源索引，数据项各有来源与许可；不计为单篇论文实现。",
    "ECRL/ECNet": "燃料性质 QSPR 工具；JOSS 2017 论文描述旧架构，当前 v4 API 以现有文档为准。",
    "LorenzoPiu/aPrioriDNS": "DNS 滤波与 a priori 评估工具；README 指向 PaSR 方法论文，软件论文尚在准备。",
    "blaiszik/blastnet-py": "BLASTNet 数据访问工具；客户端许可不替代各数据集许可。",
    "huwenfeng1128/POD-PINO": "POD/PINO 火焰模型线索；发表信息未核实，数据/权重可能需申请，代码含本地路径。",
    "HongyuanDIKyotoU/Ammonia_PINN_Net": "氨燃烧非灰辐射补偿 PINN；主题相符但 DOI 对应未确定。",
    "HongyuanDIKyotoU/FSCKPINN": "辐射 PINN 工具线索；固定提交缺少根 README 和许可。",
    "ShuaiGuo16/Data-driven-High-dimensional-UQ-Analysis": "高维燃烧模型 UQ 方法线索；未找到明确许可。",
    "ShuaiGuo16/General-Risk-Analysis-Framework": "MATLAB/UQLab 风险分析框架；论文对应和数据要求另核实。",
    "ryanxhr/DeepThermal": "工业燃烧控制强化学习，AAAI 2022 会议工作，单列为会议工具而非 JCR 期刊。",
    "mccartney-ge/GT2021-60283": "ASME Turbo Expo 会议实现线索，单列为会议资料。",
    "Ushnish-Sengupta/FYR": "ASME 会议相关燃烧工具，未定位许可。",
    "nla-group/iCRNN": "Integral CRNN，README 对应 arXiv:2609.21715；预印本不赋 JCR 分区。",
    "STFS-TUDa/oxysim-129": "燃烧机理资源，属于数据/机理支撑，不单独当作 AI 论文实现。"
}


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")


def save_json(path, content):
    write(path, json.dumps(content, ensure_ascii=False, indent=2))


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def license_name(text):
    if "educational, research, and not-for-profit purposes" in text:
        return "research-and-nonprofit-only (not OSI)", False
    if "Clear BSD License" in text:
        return "BSD-3-Clause-Clear", True
    if "Prosperity Public License" in text:
        return "Prosperity-3.0.0 (noncommercial; not OSI)", False
    if "PolyForm Noncommercial" in text:
        return "PolyForm-Noncommercial-1.0.0", False
    if "LESSER GENERAL PUBLIC LICENSE" in text:
        return ("LGPL-3.0" if re.search(r"Version 3,", text[:800]) else "LGPL-2.1") + " (inspect upstream terms)", True
    if "GNU GENERAL PUBLIC LICENSE" in text:
        return ("GPL-2.0" if re.search(r"Version 2,", text[:800]) else "GPL-3.0") + " (inspect upstream terms)", True
    if "Apache License" in text and "Version 2.0" in text:
        return "Apache-2.0", True
    if "Permission is hereby granted, free of charge" in text:
        return "MIT", True
    if "Redistribution and use in source and binary forms" in text and "Neither the name" in text:
        return "BSD-3-Clause", True
    return "unclassified_license_review_required", False


def packages(curated):
    support = dict(SUPPORT)
    support.update(json.loads((ROOT / "literature/open_support_packages.json").read_text(encoding="utf-8")))
    repositories = set(support) | {item["repository"] for item in curated.values()}
    output = []
    for repository in sorted(repositories, key=str.casefold):
        source = ROOT / "evidence/upstream" / (repository.replace("/", "__") + ".json")
        if not source.exists():
            continue
        data = json.loads(source.read_text(encoding="utf-8"))
        key = repository.replace("/", "__")
        entry = {"id": key, "repository": repository, "url": data["url"], "commit": data.get("commit"), "retrieved_at": data.get("api_checked_at", data.get("retrieved_at")), "relationship": "supporting_tool", "paper_dois": sorted(doi for doi, item in curated.items() if item["repository"] == repository), "note": support.get(repository, "论文对应与入口见关联论文卡。"), "license": "not_located", "redistribution_enabled": False, "execution_status": "not_executed", "inspection_evidence": source.relative_to(ROOT).as_posix()}
        if entry["paper_dois"]:
            entry["relationship"] = "paper_link_reviewed"
        if data.get("license_path"):
            license_source = ROOT / data["license_path"]
            if not license_source.exists():
                license_source = ROOT / "code_packages" / key / "UPSTREAM_LICENSE.txt"
            text = license_source.read_bytes().decode("utf-8")
            entry["license"], entry["redistribution_enabled"] = license_name(text)
            entry["license_url"] = data["license_url"]
            entry["license_sha256"] = hashlib.sha256(text.encode()).hexdigest()
            license_target = ROOT / "code_packages" / key / "UPSTREAM_LICENSE.txt"
            license_target.parent.mkdir(parents=True, exist_ok=True)
            license_target.write_bytes(text.encode("utf-8"))
        if entry["commit"]:
            entry["pinned_url"] = data["url"] + "/tree/" + entry["commit"]
            entry["archive_url"] = "https://api.github.com/repos/" + repository + "/tarball/" + entry["commit"]
        entry["readme_source"] = data.get("readme_url")
        archive_record = ROOT / "code_packages" / key / "archive.json"
        if archive_record.exists():
            archive = json.loads(archive_record.read_text(encoding="utf-8"))
            entry["archive"] = archive
            if archive.get("status") == "downloaded":
                entry["collection_status"] = "source_archive_collected"
        snapshot_record = ROOT / "code_packages" / key / "source_snapshot.json"
        if snapshot_record.exists():
            snapshot = json.loads(snapshot_record.read_text(encoding="utf-8"))
            entry["source_snapshot"] = snapshot
            if snapshot.get("status") == "collected":
                entry.setdefault("collection_status", "partial_source_snapshot_collected")
        entry.setdefault("collection_status", "pinned_link_and_license" if entry["redistribution_enabled"] else "link_only")
        demo_path = ROOT / "reproductions/C01_wsgg_author_demo/results/metrics.json"
        if demo_path.exists() and repository == "TaoRen-Rad/WSGG-H2O-CO2-NH3":
            entry["execution_status"] = "author_demo_executed"
            entry["execution_evidence"] = demo_path.relative_to(ROOT).as_posix()
        subcase_path = ROOT / "reproductions/C02_flamepinn_case1/results/metrics.json"
        if subcase_path.exists() and repository == "CAME-THU/FlamePINN-1D":
            entry["execution_status"] = "trained_preprint_subcase_compared"
            entry["execution_evidence"] = subcase_path.relative_to(ROOT).as_posix()
        output.append(entry)
    return output


def main():
    curated = json.loads((ROOT / "literature/curation.json").read_text(encoding="utf-8"))
    curated.update(json.loads((ROOT / "literature/open_work_additions.json").read_text(encoding="utf-8")))
    candidate_source = ROOT / "literature/screened_candidates.json"
    if not candidate_source.exists():
        candidate_source = ROOT / "catalog/papers.json"
    candidates = json.loads(candidate_source.read_text(encoding="utf-8"))
    candidates = [paper for paper in candidates if not re.search(r"wildfire|wildland|forest.fire|vegetation.fire|landscape.fire|burned.area|burnt.area|satellite|remote.sens|global.fire", paper["title"], re.I)]
    code_packages = packages(curated)
    package_index = {item["repository"]: item for item in code_packages}
    journals = {item["journal"]: item for path in (ROOT / "evidence/journals").glob("*.json") if (item := json.loads(path.read_text(encoding="utf-8")))}
    papers = []
    for candidate in candidates:
        doi = candidate["doi"]
        raw = candidate["metadata"]
        note = curated.get(doi, {})
        journal = journals.get(candidate["journal"], {})
        quartile = journal.get("reported_best_quartile") if journal.get("identity_in_page") else None
        uncertain = candidate["journal"] == "Applications in Energy and Combustion Science"
        status = "provisional_q1_q2" if quartile in ["Q1", "Q2"] and not uncertain else "adjacent_q3_q4" if quartile in ["Q3", "Q4"] else "pending_jcr"
        paper_id = "P" + hashlib.sha256(doi.encode()).hexdigest()[:10]
        category = note.get("category", candidate["category"])
        subcategory = note.get("subcategory", candidate["subcategory"])
        repository = note.get("repository")
        package = package_index.get(repository, {})
        search_file = ROOT / "evidence/code_search" / (hashlib.sha256(doi.encode()).hexdigest()[:12] + ".json")
        search = json.loads(search_file.read_text(encoding="utf-8")) if search_file.exists() else {}
        path = ("literature/adjacent/" + paper_id) if status == "adjacent_q3_q4" else (category + "/" + subcategory + "/" + paper_id)
        paper = {"id": paper_id, "doi": doi, "title": candidate["title"], "year": candidate["year"], "journal": candidate["journal"], "authors": [" ".join(filter(None, [author.get("given"), author.get("family")])) or author.get("name", "") for author in raw.get("author", [])], "category": category, "subcategory": subcategory, "path": path, "doi_url": "https://doi.org/" + doi, "metadata_source": "https://api.crossref.org/works/" + doi, "metadata_retrieved_date": DATE, "reading_level": "metadata_and_upstream_readme" if note else "title_screen_only_fulltext_pending", "screening": "candidate_not_systematic_review_inclusion", "scope": "combustion_and_adjacent_thermal_conversion", "jcr": {"status": status, "reported_best_quartile": quartile, "edition": journal.get("jcr_edition"), "officially_verified": False, "categories": journal.get("categories", []), "source_url": journal.get("source_url"), "source_type": journal.get("source_type", "not_located"), "caution": "JCR edition unknown; best of reported categories; not necessarily Q1 in Energy & Fuels." + (" Secondary table has possible duplicated-category issue; kept pending." if uncertain else "")}, "code": {"status": "reviewed_paper_link" if note else "search_hits_unverified" if search.get("items") else "searched_no_confirmed_match" if search and not search.get("error") else "search_error" if search.get("error") else "not_searched_per_doi", "repository": repository, "relationship": note.get("relationship"), "commit": package.get("commit"), "license": package.get("license"), "package_id": package.get("id"), "search_hits": search.get("total_count"), "search_evidence": search_file.relative_to(ROOT).as_posix() if search_file.exists() else None}, "reproduction": {"status": "not_executed", "paper_metrics_reproduced": False}, "curated_note": note or None, "metadata": raw}
        if "�" in paper["title"]:
            paper["metadata_warning"] = "Crossref title contains replacement characters; original retained; verify publisher title before publication citation."
        if package.get("execution_status") == "author_demo_executed":
            paper["reproduction"]["status"] = "author_demo_executed_not_paper_metric_reproduction"
            paper["reproduction"]["evidence"] = package["execution_evidence"]
        if package.get("execution_status") == "trained_preprint_subcase_compared":
            paper["reproduction"]["status"] = "trained_preprint_subcase_compared"
            paper["reproduction"]["evidence"] = package["execution_evidence"]
        papers.append(paper)
    papers.sort(key=lambda item: (-item["year"], item["category"], item["doi"]))
    save_json("catalog/papers.json", papers)
    save_json("catalog/code_packages.json", code_packages)
    counts = collections.Counter(paper["jcr"]["status"] for paper in papers)
    stats = {"date": DATE, "candidate_papers": len(papers), "recent_2024_2026": sum(paper["year"] >= 2024 for paper in papers), "jcr_officially_verified": 0, "quartile_status": dict(counts), "reviewed_paper_code_links": sum(bool(paper["curated_note"]) for paper in papers), "code_packages": len(code_packages), "licensed_for_collection": sum(item["redistribution_enabled"] for item in code_packages), "archives_collected": sum(item["collection_status"] == "source_archive_collected" for item in code_packages), "executed_independent_baselines": 2, "published_paper_metrics_reproduced": 0}
    stats["executed_author_demos"] = sum(item["execution_status"] == "author_demo_executed" for item in code_packages)
    stats["unique_packages_with_source"] = sum(item["collection_status"] in {"source_archive_collected", "partial_source_snapshot_collected"} for item in code_packages)
    stats["trained_preprint_subcases"] = sum(item["execution_status"] == "trained_preprint_subcase_compared" for item in code_packages)
    stats["partial_source_snapshots_collected"] = sum(item.get("source_snapshot", {}).get("status") == "collected" for item in code_packages)
    save_json("catalog/stats.json", stats)
    csv_fields = ["id", "year", "title", "journal", "doi", "category", "subcategory", "jcr_status", "reported_best_quartile", "jcr_edition", "officially_verified", "reading_level", "code_status", "repository", "license", "path"]
    for filename, selected in [("papers.csv", papers), ("q1_q2_provisional.csv", [paper for paper in papers if paper["jcr"]["status"] == "provisional_q1_q2"]), ("pending_jcr.csv", [paper for paper in papers if paper["jcr"]["status"] == "pending_jcr"]), ("adjacent_q3_q4.csv", [paper for paper in papers if paper["jcr"]["status"] == "adjacent_q3_q4"])]:
        with (ROOT / "catalog" / filename).open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=csv_fields)
            writer.writeheader()
            for paper in selected:
                writer.writerow({**{key: paper[key] for key in ["id", "year", "title", "journal", "doi", "category", "subcategory", "reading_level", "path"]}, "jcr_status": paper["jcr"]["status"], "reported_best_quartile": paper["jcr"]["reported_best_quartile"], "jcr_edition": "unknown", "officially_verified": False, "code_status": paper["code"]["status"], "repository": paper["code"]["repository"], "license": paper["code"]["license"]})
    bib = []
    for paper in papers:
        def escape(value):
            return str(value).replace("\\", "\\textbackslash{}").replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
        bib.append("@article{" + paper["id"] + ",\n" + ",\n".join("  " + key + " = {" + escape(value) + "}" for key, value in [("title", paper["title"]), ("author", " and ".join(paper["authors"])), ("journal", paper["journal"]), ("year", paper["year"]), ("doi", paper["doi"]), ("url", paper["doi_url"]), ("note", "Candidate; JCR edition unverified; see catalog record")]) + "\n}")
    write("catalog/references.bib", "\n\n".join(bib))
    for paper in papers:
        depth = len(pathlib.PurePosixPath(paper["path"]).parts)
        back = "../" * depth
        direction = DIRECTIONS[paper["category"]]
        author_text = "; ".join(paper["authors"])
        lines = ["# " + paper["title"], "", f"{paper['id']} · {paper['year']} · {paper['journal']}", "", f"作者：{author_text}", "", f"- DOI：[原文入口]({paper['doi_url']})", f"- 分类：{direction['name']} / {direction['sub'].get(paper['subcategory'], paper['subcategory'])}", f"- JCR：**{STATUS[paper['jcr']['status']]}**；报告最佳分区 {paper['jcr']['reported_best_quartile'] or '未知'}；版本未知；官方核实：否。", f"- 阅读深度：{'已核对元数据与上游 README，尚未完成全文精读' if paper['curated_note'] else '标题与元数据筛选，待摘要/全文复核'}。", "- 论文原始指标复现：**未执行**。", f"- [统一方法与证据等级]({back}docs/METHODOLOGY.md) · [方向说明]({back}{paper['category']}/README.md) · [全局地图]({back}00_literature_map/README.md)"]
        lines = [line.replace("论文原始指标复现：**未执行**", "完整期刊论文复现：**尚未验收**") for line in lines]
        if paper["reproduction"]["status"] == "trained_preprint_subcase_compared":
            lines += ["", f"此前已完成预印本单工况训练：[C02 协议、误差和局限]({back}reproductions/C02_flamepinn_case1/README.md)。期刊全文指标复现仍未完成。"]
        elif paper["reproduction"].get("evidence"):
            lines += ["", f"已执行作者演示：[命令、数值和适配记录]({back}reproductions/C01_wsgg_author_demo/README.md)；尚未重训或对照原文表格。"]
        if paper.get("metadata_warning"):
            lines += ["", "元数据提醒：题名含 Crossref 原始乱码；请以出版商页面核对，未擅自改写题名。"]
        if paper["jcr"]["source_url"]:
            lines += ["", f"分区线索：[二级来源]({paper['jcr']['source_url']})。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。"]
        if paper["curated_note"]:
            note = paper["curated_note"]
            for title, key in [("研究问题", "problem"), ("方法与代码所能确认的内容", "method"), ("复现入口与依赖", "entry"), ("环境与数据", "dependencies"), ("建议验证协议（本库设计）", "evaluation"), ("局限与当前状态", "limitations")]:
                lines += ["", "## " + title, "", note[key]]
            package = package_index[note["repository"]]
            lines += ["", "## 代码溯源", "", f"- 仓库：[{package['repository']}]({package['url']})", f"- 固定提交：`{package['commit']}`", f"- 关系证据：`{note['relationship']}`；来自上游 README，不代表本库已做作者身份独立认证。", f"- 许可：{package['license']}；收纳状态：`{package['collection_status']}`。", f"- [代码包卡片]({back}code_packages/{package['id']}/README.md)"]
        else:
            lines += ["", "## 这条记录目前能说明什么", "", "标题和期刊元数据表明它可能属于本方向；本卡不提供未经全文核实的架构、数据量、速度提升或结论。下列内容是该方向的阅读问题与复现设计，不是对本文结果的转述。", "", "## 精读与复现提取清单", "", f"1. 明确本文的物理目标：{direction['question']}", f"2. 提取数据生成/测量协议：{direction['data']}", f"3. 对照原文确认切分：{direction['split']}", f"4. 找到原文表/图及指标定义：{direction['metrics']}", "5. 记录完整依赖、机理/数据许可证、随机种子、设备、训练预算和失败运行。", "6. 建立公式—代码对应表，先运行最小基线，再对同一数据切分复现目标图表。", "", "## 代码检索状态", "", f"`{paper['code']['status']}`。DOI 精确 GitHub README 检索会漏掉未写 DOI 的实现；搜到引用也不能认定为本文代码。未确认实现不意味着作者没有开源。"]
        lines += ["", "## 待完成的学术核验", "", "- 官方 JCR 年份、类别、排名与分区证据。", "- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。", "- 代码—论文版本一致性，数据及预训练权重是否齐全。", "- 论文指标同口径复现及差异分析。", "", f"元数据来源：[Crossref]({paper['metadata_source']})；本轮整理日期 {DATE}。完整元数据见同目录 `paper.json`。"]
        write(paper["path"] + "/README.md", "\n".join(lines))
        save_json(paper["path"] + "/paper.json", {key: value for key, value in paper.items() if key != "metadata"})
    for category, direction in DIRECTIONS.items():
        selected = [paper for paper in papers if paper["category"] == category and paper["jcr"]["status"] != "adjacent_q3_q4"]
        lines = ["# " + direction["name"], "", direction["plain"], "", f"本目录含 {len(selected)} 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。", "", "[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)"]
        for heading, key in [("核心问题", "question"), ("方法演进与比较", "methods"), ("数据与物理定义", "data"), ("怎样判断模型有效", "metrics"), ("如何避免数据泄漏", "split"), ("主要局限与选题问题", "limits"), ("建议阅读和实践路径", "route")]:
            lines += ["", "## " + heading, "", direction[key]]
        lines += ["", "## 细分类与论文索引", "", "分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。"]
        for subcategory, label in direction["sub"].items():
            subset = [paper for paper in selected if paper["subcategory"] == subcategory]
            lines += ["", f"### [{label}]({subcategory}/README.md)（{len(subset)}）", "", "| 年份 | 论文 | 分区线索 | 代码 |", "|---|---|---|---|"]
            rows = [f"| {paper['year']} | [{md(paper['title'])}]({subcategory}/{paper['id']}/README.md) | {paper['jcr']['reported_best_quartile'] if paper['jcr']['status'] == 'provisional_q1_q2' else 'Q?'} | {'✓' if paper['curated_note'] else '待核对'} |" for paper in subset]
            lines += rows
            sublines = ["# " + label, "", direction["plain"], "", "[方向说明](../README.md)", "", "| 年份 | 论文 | DOI |", "|---|---|---|"]
            sublines += [f"| {paper['year']} | [{md(paper['title'])}]({paper['id']}/README.md) | [{paper['doi']}]({paper['doi_url']}) |" for paper in subset]
            write(category + "/" + subcategory + "/README.md", "\n".join(sublines))
        write(category + "/README.md", "\n".join(lines))
    for package in code_packages:
        related = [paper for paper in papers if paper["doi"] in package["paper_dois"]]
        lines = ["# " + package["repository"], "", package["note"], "", f"- [原始仓库]({package['url']}) · [固定版本]({package.get('pinned_url', package['url'])})", f"- 提交：`{package['commit'] or '未取得'}`", f"- 许可：**{package['license']}**。", f"- 收纳状态：`{package['collection_status']}`；执行状态：`{package['execution_status']}`。", "- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。", "", "## 关联论文与入口", ""]
        lines += [f"- [{paper['title']}](../../{paper['path']}/README.md) — {paper['doi']}" for paper in related] or ["具体期刊论文对应关系尚未建立；按支撑工具、会议或预印本处理。"]
        if package.get("readme_source"):
            lines += ["", f"[上游 README（固定版本）]({package['readme_source']})"]
        if package.get("license_url"):
            lines += ["", f"## 许可证与再分发", "", f"[上游许可]({package['license_url']})；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。"]
        if package["redistribution_enabled"]:
            lines += ["", "## 获取固定版本", "", "在仓库根目录执行：", "", "```powershell", f"python tools/fetch_packages.py --package {package['id']}", "```", "", "下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。"]
        else:
            lines += ["", "## 获取限制", "", "未定位明确许可或许可受限，本库不镜像代码。请按原作者条款获取；不能把 GitHub 可见等同于允许再分发。"]
        if package.get("archive", {}).get("status") == "downloaded":
            archive = package["archive"]
            lines += ["", f"已收纳文件：[{pathlib.Path(archive['path']).name}]({pathlib.Path(archive['path']).name})；大小 {archive['bytes']} bytes；SHA-256 `{archive['sha256']}`。"]
        elif package.get("archive", {}).get("error"):
            lines += ["", "完整归档本轮未收纳：`" + package["archive"]["error"] + "`。这不表示上游未提供代码；固定下载入口仍可使用。"]
        if package.get("source_snapshot", {}).get("status") == "collected":
            snapshot = package["source_snapshot"]
            lines += ["", "## 部分源码快照", "", f"已收纳 [{pathlib.Path(snapshot['path']).name}]({pathlib.Path(snapshot['path']).name})，含 {len(snapshot['files'])} 个源码/配置/说明/许可文件；SHA-256 `{snapshot['sha256']}`。", "", "这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。"]
        elif package.get("source_snapshot", {}).get("error"):
            lines += ["", "部分源码快照本轮失败：`" + package["source_snapshot"]["error"] + "`；未将其计为已收纳。"]
        write("code_packages/" + package["id"] + "/README.md", "\n".join(lines))
        save_json("code_packages/" + package["id"] + "/manifest.json", package)
    package_lines = ["# 固定版本代码包索引", "", "一个仓库只计一个包；一个包可能关联多篇论文。可见源码、OSI 开源、数据可用和执行成功分别记录。", "", "[下载与许可规范](../docs/CODE_COLLECTION.md) · [返回首页](../README.md)", "", "| 包 | 许可 | 收纳 | 关联 DOI 数 |", "|---|---|---|---|"]
    package_lines += [f"| [{item['repository']}]({item['id']}/README.md) | {item['license']} | {item['collection_status']} | {len(item['paper_dois'])} |" for item in code_packages]
    write("code_packages/README.md", "\n".join(package_lines))
    write("literature/adjacent/README.md", "# 不纳入 Q1/Q2 候选主集的分区条目\n\n这些条目被二级来源报告为 Q3/Q4，仍保留以便核验和避免重复检索。JCR 版本未知，不表示其历史各年均为此分区。\n\n" + "\n".join(f"- [{paper['title']}]({paper['id']}/README.md) · {paper['journal']}" for paper in papers if paper["jcr"]["status"] == "adjacent_q3_q4"))
    save_json("catalog/journals.json", list(journals.values()))
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
