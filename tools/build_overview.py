import collections
import html
import json
import pathlib

from build_catalog import DATE, DIRECTIONS, ROOT, STATUS, md, write


def table(papers, back="../"):
    lines = ["| 年份 | 论文 | 方向 | 分区状态 | 代码 |", "|---|---|---|---|---|"]
    for paper in papers:
        lines.append(f"| {paper['year']} | [{md(paper['title'])}]({back}{paper['path']}/README.md) | {DIRECTIONS[paper['category']]['name']} | {paper['jcr']['status']} | {'已核对链接' if paper['curated_note'] else '待核对'} |")
    return "\n".join(lines)


def main():
    papers = json.loads((ROOT / "catalog/papers.json").read_text(encoding="utf-8"))
    stats = json.loads((ROOT / "catalog/stats.json").read_text(encoding="utf-8"))
    screening = json.loads((ROOT / "evidence/screening.json").read_text(encoding="utf-8"))
    packages = json.loads((ROOT / "catalog/code_packages.json").read_text(encoding="utf-8"))
    main_papers = [paper for paper in papers if paper["jcr"]["status"] != "adjacent_q3_q4"]
    readme = f"""# AI + Combustion｜燃烧人工智能文献与代码库

面向燃烧、反应流和热安全研究的中文研究入口：按 **物理方向 → 子方向 → 论文** 组织文献，收纳可追溯的代码，并保留真实实验结果。优先关注新方法，同时保留理解新方法需要的经典路线。

**整理日期：{DATE}。只采用 JCR 分区。** 本轮没有取得版本明确的官方 JCR 记录，因此以下是候选库，不能把全部条目称为“已确认一区/二区”。多数论文仍处于题名/元数据筛选阶段；详细状态见每张论文卡。

## 本轮规模与完成度

| 项目 | 数量 | 解释 |
|---|---:|---|
| 检索命中 / DOI 去重记录 | {screening['retrieved_hits']} / {screening['unique_records']} | 保留检索式、时间与排除原因 |
| AI×燃烧及相邻热转化候选 | {stats['candidate_papers']} | 不是全部已精读或有代码 |
| 2024–2026 年候选 | {stats['recent_2024_2026']} | 年份来自 Crossref published |
| 二级来源报告 Q1/Q2 | {stats['quartile_status'].get('provisional_q1_q2',0)} | JCR 版本待官方核实 |
| 分区待核实 | {stats['quartile_status'].get('pending_jcr',0)} | 单独排队，不默认 Q1 |
| 二级来源 Q3/Q4 附录 | {stats['quartile_status'].get('adjacent_q3_q4',0)} | 不纳入候选主目录 |
| 已核对论文—代码链接 | {stats['reviewed_paper_code_links']} | 含实现、支撑组件及教程，关系逐篇区分 |
| 代码/支撑工具仓库 | {stats['code_packages']} | 一仓库多文只计一个包 |
| 明确可再分发许可 / 已附源归档 | {stats['licensed_for_collection']} / {stats['archives_collected']} | 其余为固定链接或许可受限 |
| 已附部分源码快照 | {stats.get('partial_source_snapshots_collected',0)} | 不包含完整数据/权重，另记数量 |
| 已执行独立基线 / 原文指标复现 | 2 / 0 | 不将独立基线冒充论文复现 |
| 已执行作者演示 | {stats.get('executed_author_demos',0)} | 固定版本和原始数据推理，未重训 |

统计源：[stats.json](catalog/stats.json)。这是有检索边界的一轮整理，没有数量上限，但也没有证明覆盖所有文献。OA 论文、可见源码、有许可代码、数据权重齐备和复现成功分别记录。

## 从哪里开始

1. **快速建立全景**：[思维导图和阅读路线](00_literature_map/README.md)，再看 [方法×物理问题矩阵](00_literature_map/METHOD_PROBLEM_MATRIX.md)。
2. **找论文**：[全部论文索引](00_literature_map/ALL_PAPERS.md)、[2024–2026 新文献](00_literature_map/RECENT_2024_2026.md)、[本地交互检索页](00_literature_map/explorer.html)。交互页下载后用浏览器打开，GitHub 页面本身只显示源码。
3. **找可操作的代码**：[代码包清单](code_packages/README.md) 和 [已核对论文代码路线](00_literature_map/CODE_READING_ROUTE.md)。
4. **跑透明的最小实验**：[B01 氢气点火代理](reproductions/B01_hydrogen_ignition/README.md) 与 [B02 Bratu PINN](reproductions/B02_bratu_pinn/README.md)。
5. **开展正式复现**：先读 [复现协议](docs/REPRODUCTION_PROTOCOL.md)，明确原文图表、数据、切分和指标，再推进训练。

初次接触这些方法，可先读 [术语、指标与论文阅读指南](docs/GLOSSARY.md)，理解 PINN、LES、神经算子和误差数字的实际含义。

已执行的上游期刊代码：[C01 氨燃烧 PINN-WSGG 辐射演示](reproductions/C01_wsgg_author_demo/README.md)，含逐点数值、误差定义和适配说明。

## 大方向导航

| 目录 | 研究问题 | 候选数 |
|---|---|---:|
"""
    for category, direction in DIRECTIONS.items():
        count = sum(paper["category"] == category for paper in main_papers)
        readme += f"| [{direction['name']}]({category}/README.md) | {direction['plain']} | {count} |\n"
    readme += """
每个方向的 README 包括核心问题、方法演进、数据、评价指标、切分、局限和建议阅读顺序。子方向目录包含论文列表；每篇 `README.md` 与 `paper.json` 保存 DOI、作者、来源、分区状态、代码证据和复现待办。交叉方法用交互页检索；自动分类需在精读时继续修订。

## 目录结构

```text
00_literature_map/              全景图、矩阵、逐方向文献表、交互浏览器
01_chemistry_kinetics/          方向 → 子方向 → DOI 稳定 ID → README/paper.json
02_turbulence_closure/ ...      其余九个研究方向
code_packages/                 固定提交、许可、包说明与可收纳源归档
reproductions/                 独立基线/后续复现实验、原始输出与环境
catalog/                       JSON、UTF-8 CSV、BibTeX、期刊与统计
literature/curation.json        人工核对的代码论文说明与分类覆盖
literature/adjacent/            Q3/Q4 线索附录，不计入主方向候选
evidence/                      检索、排除、分区、上游与代码搜索证据
docs/                          范围、许可、方法与复现规范
tools/                         检索、建库、下载、校验和维护脚本
```

## 本地使用

```powershell
git clone https://github.com/Yihong-Song/AI-combustion.git
cd AI-combustion
python -m pip install -r requirements-tools.txt
python tools/validate.py
python tools/fetch_packages.py
```

离线重建、扩充检索和逐文复现步骤见 [维护指南](docs/MAINTENANCE.md)；[本地校验报告](evidence/validation.json)记录实际检查范围。

科学基线需另装 `requirements-baselines.txt`。历史代码应使用各自环境，不能将旧 TensorFlow、Julia、OpenFOAM 依赖混装在同一环境。源归档只下载不自动运行。

## 数据下载与引用

- [papers.csv](catalog/papers.csv) / [papers.json](catalog/papers.json)：全部候选和完整状态。
- [Q1/Q2 二级线索候选](catalog/q1_q2_provisional.csv) / [分区待核实](catalog/pending_jcr.csv) / [Q3/Q4 附录](catalog/adjacent_q3_q4.csv)。
- [BibTeX](catalog/references.bib)：用于导入文献管理器，题名、作者、年份仍需在投稿前核对出版商；保留候选注记。
- [期刊分区证据表](00_literature_map/JCR_EVIDENCE.md)：逐期刊保留类别与来源。

引用研究结论时应引用原论文，使用代码时按上游要求引用论文并遵守许可。本库没有转载付费全文，没有将二级分区网页当作官方证明。

## 当前局限与后续维护

题名筛选会漏掉摘要才出现 AI 的论文，也会保留需进一步审查的热解/燃料性质边界条目。Crossref、GitHub、分区网页覆盖有限，网络失败和查询数量上限均会造成遗漏。已核对代码论文的说明主要依据元数据和 README，尚未完成全部原文精读。当前不应将本库直接作为“所有 Q1/Q2 文献”或全面系统综述的结论依据。

下一阶段优先补官方 JCR 版本、全文提取、数据与权重核验，然后按同口径协议复现目标图表。[方法全文](docs/METHODOLOGY.md) · [代码收纳与许可](docs/CODE_COLLECTION.md) · [建设记录](PLAN.md)。
"""
    write("README.md", readme)
    mindmap = ["mindmap", "  root((AI × 燃烧))"]
    for category, direction in DIRECTIONS.items():
        count = sum(paper["category"] == category for paper in main_papers)
        mindmap.append("    " + direction["name"] + " " + str(count))
        mindmap.extend("      " + label for label in direction["sub"].values())
    overview = """# 燃烧 AI 文献思维导图与研究导航

这张图按物理问题组织，方法横跨分支。它概括本轮检索到的研究版图，不能解释为已经穷尽或全文核实的所有 Q1/Q2 文章。分区采用 JCR 线索，官方版本仍待核实。

```mermaid
""" + "\n".join(mindmap) + "\n```\n\n"
    overview += """## 怎样读这张图

燃烧 AI 常见的目标可以分成四类：替代昂贵计算、从观测恢复状态、从数据发现/校准规律、进行预测与控制。先选目标，再选网络；相同 PINN、CNN 或 Transformer 在不同物理任务上的可比性通常有限。

1. 入门先阅读综述与 B01/B02，理解数据、单位、切分和指标。
2. 若关注 CFD 成本，沿化学代理 → 湍流闭合 → 神经算子阅读。
3. 若关注实验，沿光谱/层析 → 不稳定性辨识 → 控制阅读。
4. 若关注新燃料与安全，沿燃料性质 → 氢氨着火 → 热解/热失控与不确定度阅读。

## 全量与专题入口

- [逐方向全部论文](ALL_PAPERS.md)：含待核实状态；Q3/Q4 单独附录。
- [2024–2026 年新文献](RECENT_2024_2026.md)：按方向组织，保留 DOI 与论文卡。
- [方法×问题×数据矩阵](METHOD_PROBLEM_MATRIX.md)：理解任务与评价，避免只按模型名字追热点。
- [代码优先阅读路线](CODE_READING_ROUTE.md)：目前已核对论文—代码的工作。
- [研究问题与证据缺口](RESEARCH_QUESTIONS.md)：可验证的研究设计，不把检索未见说成全球空白。
- [JCR 类别证据](JCR_EVIDENCE.md)：解释多类别分区、二级来源和待核实条目。
- [本地交互检索](explorer.html)：搜索题名/作者/DOI，筛选年份、方向、分区和代码。

## 分支详解

"""
    for category, direction in DIRECTIONS.items():
        overview += f"- [{direction['name']}](branches/{category}.md)：{direction['plain']}\n"
        selected = [paper for paper in main_papers if paper["category"] == category]
        lines = ["# " + direction["name"], "", direction["plain"], "", "[返回全景](../README.md) · [方向技术说明](../../" + category + "/README.md)", "", "## 物理目标与评价逻辑", "", direction["question"], "", direction["metrics"], "", "## 方法与数据", "", direction["methods"], "", direction["data"], "", "## 风险与阅读路线", "", direction["limits"], "", direction["route"]]
        for subcategory, label in direction["sub"].items():
            subset = [paper for paper in selected if paper["subcategory"] == subcategory]
            lines += ["", "## " + label, "", table(subset, "../../")]
        write("00_literature_map/branches/" + category + ".md", "\n".join(lines))
    write("00_literature_map/README.md", overview)
    all_lines = ["# 全部文献候选索引", "", "本索引按方向分组，按年份降序。标题级筛选不等于全文纳入，分区线索不等于官方 JCR 认证。", "", "[返回思维导图](README.md) · [Q3/Q4 附录](../literature/adjacent/README.md)"]
    recent_lines = ["# 2024–2026 年研究线索", "", f"共 {stats['recent_2024_2026']} 条（含 Q3/Q4 附录中的新文，主表仅列非 Q3/Q4 候选）。日期以 Crossref published 为准；2026 条目可能为在线发表。", "", "这些标题显示了守恒、算子学习、生成模型、跨装置预警与可微反演等探索。是否优于已有方法需全文、同口径比较和实际复现，不能从标题判断。"]
    for category, direction in DIRECTIONS.items():
        selected = [paper for paper in main_papers if paper["category"] == category]
        all_lines += ["", "## " + direction["name"], "", table(selected)]
        recent_lines += ["", "## " + direction["name"], "", table([paper for paper in selected if paper["year"] >= 2024])]
    write("00_literature_map/ALL_PAPERS.md", "\n".join(all_lines))
    write("00_literature_map/RECENT_2024_2026.md", "\n".join(recent_lines))
    matrix = ["# 方法 × 物理问题 × 数据 × 评价", "", "同一网络在不同任务中不能直接排名。下表为研究设计综述，不是所有论文的全文定量汇总。", "", "| 物理方向 | 常见方法 | 数据与评价重点 |", "|---|---|---|"]
    for category, direction in DIRECTIONS.items():
        matrix.append(f"| [{direction['name']}](../{category}/README.md) | {md(direction['methods'])} | {md(direction['metrics'])} |")
    matrix += ["", "## 燃料/对象这条横轴", "", "氢/氨：差异扩散、痕量 NOx 和高压工况；烃燃料：详细化学与组分尺度跨度；生物质/煤：材料组成、升温速率与尺度效应；电池：热失控反应可辨识性；金属/固体推进剂：多相与界面。单燃料高精度并不证明跨燃料泛化。", "", "## 贯穿所有分支的比较标准", "", "物理单位一致 → 数据/机理可追溯 → 独立工况切分 → 明确传统基线 → 外推和失效分析 → 不确定度 → 全链路成本 → 后验/实验验证。多方法组合须分别做消融，不能把所有改进归因于新模型名字。"]
    write("00_literature_map/METHOD_PROBLEM_MATRIX.md", "\n".join(matrix))
    code_papers = [paper for paper in papers if paper["curated_note"]]
    write("00_literature_map/CODE_READING_ROUTE.md", "# 代码优先阅读路线\n\n先看许可与数据，再看入口。表中链接已核对，但原始训练未执行。建议顺序：轻量辐射演示 → FlamePINN 简化算例 → SL-GPS 自燃 → CMLM 预存数据 → Bayesian CRNN → 详细化学/CFD。受限或缺许可的代码只保留链接。\n\n" + table(code_papers) + "\n\n[全部代码与支撑工具](../code_packages/README.md) · [复现协议](../docs/REPRODUCTION_PROTOCOL.md)")
    journals = json.loads((ROOT / "catalog/journals.json").read_text(encoding="utf-8"))
    jcr_lines = ["# JCR 分区证据及待核实表", "", "**本轮官方 JCR 确认数为 0；所有二级来源记录的 JCR 版本均未知。** 这里只转录 JIF 类别分区，不使用 SJR、中科院分区或 JCI。最佳类别 Q1 不等于 Energy & Fuels 类别 Q1。", "", "| 期刊 | 二级最佳线索 | 官方核实 | JCR 版本 | 来源/情况 |", "|---|---|---|---|---|"]
    for journal in sorted(journals, key=lambda item: item["journal"]):
        source = journal.get("source_url")
        source_label = f"[LetPub]({source})" if source else "未取得"
        jcr_lines.append(f"| {journal['journal']} | {journal.get('reported_best_quartile') or '?'} | 否 | 未知 | {source_label}；{'身份匹配' if journal.get('identity_in_page') else '身份/数据待核实'} |")
    for journal in sorted(journals, key=lambda item: item["journal"]):
        if journal.get("categories"):
            jcr_lines += ["", "## " + journal["journal"], "", "| 类别 | 集合 | 分区线索 | 排名 |", "|---|---|---|---|"]
            jcr_lines += [f"| {md(item['category'])} | {item['collection']} | {item['quartile']} | {item['rank']} |" for item in journal["categories"]]
    jcr_lines += ["", "## 正式核验需要什么", "", "选定 JCR 版本，取得 Clarivate/学校图书馆官方记录，保存期刊身份、类别、分区、排名与证据路径；说明采用最佳类别还是相关类别。公开二级网页只能作为线索。AECS 表格可疑、Physics of Fluids 身份未匹配等条目保持 pending。"]
    write("00_literature_map/JCR_EVIDENCE.md", "\n".join(jcr_lines))
    write("00_literature_map/RESEARCH_QUESTIONS.md", """# 可检验的研究问题与证据缺口

这里的“缺口”指本库当前证据尚不充分或值得专门比较的问题，**不是声称全球尚无人研究**。相关论文由各方向索引和代码路线定位，真正选题前需完成全文追溯与前后向引文检索。

| 问题 | 为什么值得比较 | 最小可检验设计 | 不能据此断言 |
|---|---|---|---|
| 化学代理的长时守恒与稳定性 | 单步拟合误差可能在迭代中累积 | 固定同一机理、时间步、采样和参数量，比较有无守恒层、回退器及负组分率 | 守恒自动保证化学准确 |
| 氢/氨跨工况泛化 | 差异扩散和温压范围会改变训练分布 | 留出整个压力/掺混区间，验证点火、火焰速度和 NOx，而非随机留出状态点 | 一个燃料上的结果能通用 |
| 闭合模型 a priori 与 a posteriori 一致性 | 离线误差与 LES 反馈不同 | 同 DNS 滤波数据训练后，耦合相同 LES 并比较热释放、稳定性和统计量 | 高相关系数证明可部署 |
| 算子/生成模型的分辨率与几何迁移 | 神经算子名称不保证任意网格或边界泛化 | 预先留出网格、几何和燃料，检查梯度、能谱与守恒 | 视觉细节必然是真实结构 |
| 诊断模型合成到实验迁移 | 标定、噪声和视角造成域差异 | 真值可知的合成测试 + 独立实验 + 传统反演对照和不确定度传播 | 合成图像精度等于测量精度 |
| 热声预警的跨装置有效性 | 滑窗重叠易造成虚高性能 | 整装置留出、时间隔离、预设提前量和误报成本 | 某次试验准确率证明跨平台有效 |
| TGA/DSC 机理可辨识性 | 多套有效参数可拟合同一曲线 | 多升温速率联合拟合，留出气氛条件，报告参数后验及结构差异 | 学到的网络是唯一微观机理 |
| 代理优化的真实收益 | 优化器可能寻找模型误差极值 | 用固定高保真预算复核候选最优点，记录不可行解与总成本 | 代理预测最优点即真实最优点 |

## 推荐的三条实践路线

1. **低成本入门**：B01 → 分组外推/删失处理 → 守恒代理零维测试。产物应包含原始表格、失败条件和机制哈希。
2. **物理信息与诊断**：B02 → FlamePINN Case 1 → 噪声/逆参数；或 WSGG 演示 → 氨混合气辐射外推。
3. **高保真耦合**：CMLM/多尺度采样 → 一维火焰 → LES 后验。先建立传统求解器验证，再谈加速和部署。

Transformer、KAN、flow matching、Neural Operator 等新方法可作比较对象。选题依据应是明确的物理误差、数据或算力约束，而非仅替换网络。公平比较需相同数据、预算、随机种子策略和指标，并披露不收敛结果。
""")
    compact = [{"id": paper["id"], "title": paper["title"], "doi": paper["doi"], "year": paper["year"], "journal": paper["journal"], "authors": "; ".join(paper["authors"]), "category": paper["category"], "direction": DIRECTIONS[paper["category"]]["name"], "jcr": paper["jcr"]["status"], "code": bool(paper["curated_note"]), "license": paper["code"]["license"] or "未核实", "path": "../" + paper["path"] + "/README.md"} for paper in papers]
    data_text = json.dumps(compact, ensure_ascii=False).replace("<", "\\u003c")
    explorer = """<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI × 燃烧文献浏览器</title>
<style>body{font:16px/1.7 system-ui,sans-serif;color:#18283a;background:#f3f6f8;margin:0}main{max-width:1300px;margin:auto;padding:32px}h1{margin:0;color:#123b50}p{max-width:1000px}.controls{display:flex;gap:12px;flex-wrap:wrap;background:#fff;padding:18px;border-radius:12px;position:sticky;top:0;box-shadow:0 5px 20px #1231}input,select{font:inherit;padding:8px;border:1px solid #b9cbd3;border-radius:6px}input[type=search]{flex:1;min-width:260px}.card{background:white;padding:20px;margin:16px 0;border-radius:12px;border-left:4px solid #087f8c}.meta{color:#526875;font-size:14px}.tags{color:#15636c;font-size:14px}a{color:#075b79}.count{font-weight:bold}label{display:inline-flex;gap:8px;align-items:center}h2{font-size:19px;line-height:1.5;margin:4px 0}footer{margin-top:30px;color:#526875}button{font:inherit;padding:8px;background:#e6f3f5;border:1px solid #82b4bd;border-radius:6px}</style>
<main><h1>AI × 燃烧：文献导航</h1><p>按物理问题寻找论文与代码。全部是检索候选，官方 JCR 版本待核实；“代码已核对”不等于运行成功。支持离线搜索，无外部脚本和数据请求。</p>
<div class="controls"><input id="query" type="search" aria-label="检索" placeholder="题名 / DOI / 作者 / PINN / ammonia…"><select id="direction" aria-label="方向"><option value="">全部方向</option></select><select id="year" aria-label="年份"><option value="">全部年份</option></select><select id="jcr" aria-label="分区状态"><option value="">全部分区状态</option><option value="provisional_q1_q2">二级来源 Q1/Q2 候选</option><option value="pending_jcr">JCR 待核实</option><option value="adjacent_q3_q4">Q3/Q4 附录</option></select><label><input type="checkbox" id="code">仅已核对代码论文</label><button id="reset">重置</button></div>
<p class="count" id="count" aria-live="polite"></p><div id="results"></div><footer>整理：2026-11-11 · <a href="README.md">思维导图</a> · <a href="../docs/METHODOLOGY.md">证据与方法</a> · 下载整个仓库后可打开相对路径论文卡；GitHub 不直接执行此 HTML。</footer></main>
<script>const papers=__DATA__;const controls=['query','direction','year','jcr','code'].map(name=>document.getElementById(name));const [query,direction,year,jcr,code]=controls;const labels={provisional_q1_q2:'二级来源 Q1/Q2，版本待核实',pending_jcr:'JCR 待核实',adjacent_q3_q4:'Q3/Q4 附录'};function option(select,value,label){const node=document.createElement('option');node.value=value;node.textContent=label;select.append(node)}[...new Map(papers.map(paper=>[paper.category,paper.direction]))].sort().forEach(([value,label])=>option(direction,value,label));[...new Set(papers.map(paper=>paper.year))].sort((first,second)=>second-first).forEach(value=>option(year,value,value));function render(){const needle=query.value.trim().toLowerCase();const chosen=papers.filter(paper=>(!needle||[paper.title,paper.doi,paper.authors,paper.journal].join(' ').toLowerCase().includes(needle))&&(!direction.value||paper.category===direction.value)&&(!year.value||paper.year===Number(year.value))&&(!jcr.value||paper.jcr===jcr.value)&&(!code.checked||paper.code));document.getElementById('count').textContent=`显示 ${chosen.length} / ${papers.length} 条候选`;const results=document.getElementById('results');results.replaceChildren();chosen.forEach(paper=>{const card=document.createElement('article');card.className='card';const meta=document.createElement('div');meta.className='meta';meta.textContent=`${paper.year} · ${paper.journal} · ${paper.id}`;const title=document.createElement('h2');const link=document.createElement('a');link.href=paper.path;link.textContent=paper.title;title.append(link);const tags=document.createElement('div');tags.className='tags';tags.textContent=`${paper.direction} · ${labels[paper.jcr]} · ${paper.code?'代码链接已核对 / '+paper.license:'代码未确认'}`;const authors=document.createElement('div');authors.className='meta';authors.textContent=paper.authors;const doi=document.createElement('a');doi.href='https://doi.org/'+paper.doi;doi.textContent=paper.doi;doi.target='_blank';doi.rel='noopener noreferrer';card.append(meta,title,tags,authors,doi);results.append(card)})}controls.forEach(control=>control.addEventListener('input',render));document.getElementById('reset').addEventListener('click',()=>{query.value='';direction.value='';year.value='';jcr.value='';code.checked=false;render()});render();</script></html>"""
    write("00_literature_map/explorer.html", explorer.replace("__DATA__", data_text))
    print("Overview built:", stats["candidate_papers"], "papers;", stats["archives_collected"], "archives")


if __name__ == "__main__":
    main()
