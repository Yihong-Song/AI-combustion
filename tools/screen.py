import collections
import html
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
CORE = {"combustion and flame", "proceedings of the combustion institute", "progress in energy and combustion science"}
JOURNALS = CORE | {"fuel", "energy", "applied energy", "energy conversion and management", "international journal of hydrogen energy", "chemical engineering journal", "journal of computational physics", "computer physics communications", "physics of fluids", "journal of fluid mechanics", "flow, turbulence and combustion", "combustion theory and modelling", "combustion science and technology", "applications in energy and combustion science", "mechanical systems and signal processing", "aerospace science and technology", "applied thermal engineering", "international journal of heat and mass transfer", "experimental thermal and fluid science", "measurement", "optics express", "optics and lasers in engineering", "optics letters", "applied optics", "experiments in fluids", "physical chemistry chemical physics", "scientific reports", "nature communications", "science advances", "energy & fuels", "journal of analytical and applied pyrolysis", "journal of quantitative spectroscopy and radiative transfer", "computers & chemical engineering", "reliability engineering & system safety", "proceedings of the royal society a: mathematical, physical and engineering sciences", "royal society open science", "physical review fluids", "international journal of mechanical sciences"}
AI = re.compile(r"learn|neural|data.driven|gaussian.process|random.forest|support.vector|surrogate.model|artificial.intelligence|bayesian.optim|autoencoder|generative|transformer|kolmogorov.arnold|\bKAN\b|\bPINN|\bFNO\b|\bDeepONet|\bCNN\b|\bLSTM\b|\bRNN\b|\bANN\b|\bCRNN\b|reinforcement|symbolic.regression|reservoir.comput|\bXGBoost\b", re.I)
COMBUSTION = re.compile(r"combust|flame|ignition|thermoacoustic|soot|detonat|pyrolys|fire|chemical.kinetic|reaction.kinetic|reacting.flow|reactive.flow|laminar.burning|heat.release|fuel|spray|arrhenius|chemical.reaction|stiff.chemical|\bNOx\b", re.I)


def classify(title):
    lower = title.lower()
    if re.search(r"review|principles, progress|scientific machine learning in combustion|blastnet|benchmark", lower):
        return "10_reviews_methods", "01_reviews_datasets"
    if re.search(r"thermo.?acoustic|combustion instabil|flame dynamics|flame response|flame transfer|rijke", lower):
        return "04_instability_control", "02_control" if re.search(r"control|reinforcement|suppress|mitigat", lower) else "01_prediction_identification"
    if re.search(r"radiati|radiative|spectroscop|\bcars\b|\btomograph|\bplif|\bchemilum|temperature.*reconstruct|soot.*reconstruct|\bimage|\bimaging|\bvision|\bdenois|diagnos|schlieren|segmentation|multi.speciation|soot.*inversion", lower):
        return "05_diagnostics_radiation", "02_radiation_soot" if re.search(r"radiati|radiative|soot", lower) else "01_optical_inverse"
    if re.search(r"pyrolys|biomass|coal|solid.fuel|wood|wildfire|fire.heat|firebrand|polymer|thermal.runaway|battery", lower):
        return "08_solid_fuels_fire", "01_kinetics_fire"
    if re.search(r"solid.propellant|condensed.combustion|\bhtpb\b|al.zr|magnesium.alloy", lower):
        return "08_solid_fuels_fire", "02_metals_propellants"
    if re.search(r"kinetic|chemistry|chemical|reaction|mechanism|arrhenius|stiff|rate.constant|global.pathway|neural.network.potential", lower):
        if re.search(r"discover|pathway|reaction.network|reaction neural|inferen|optimiz.*mechanism|mechanism.*optimiz|calibrat|parameter.estim", lower):
            return "01_chemistry_kinetics", "02_discovery_calibration"
        return "01_chemistry_kinetics", "01_surrogates_reduction"
    if re.search(r"supersonic|detonat|scramjet|ramjet", lower):
        return "07_engineering_design", "03_supersonic_detonation"
    if re.search(r"spray|inject|droplet|liquid.jet|jet.imping|atomiz|fuel.vapour", lower):
        return "07_engineering_design", "04_sprays_injection"
    if re.search(r"engine|boiler|gas.turbine|rocket|combustor|furnace|burner|design|optim|emission|\bnox\b|free.piston", lower):
        return "07_engineering_design", "02_control_optimization" if re.search(r"control|optim|design|reinforce", lower) else "01_performance_emissions"
    if re.search(r"operator|fourier|deeponet|super.resol|generative.adversarial|\bgan\b|autoencoder|reduced.order|latent|manifold|modal|koopman|dimensionality.reduction|\bpod\b", lower):
        return "03_operators_reconstruction", "01_operators_rom"
    if re.search(r"closure|subgrid|subfilter|sub.filter|turbulen|\bles\b|filtered.density|probability.density|mixing|flamelet|wrinkling|regime.identification|flame.type|combustion.regime|lift.off", lower):
        return "02_turbulence_closure", "01_closures_manifolds"
    if re.search(r"physics.informed|pinn|inverse|differentiab", lower):
        return "06_physics_informed", "01_forward_inverse"
    if re.search(r"hydrogen|ammonia|ignition|flame.speed|burning.velocity|octane|cetane|fuel|sooting.tendenc|flash.point|flashpoint|viscosit|heat.of.combustion", lower):
        return "09_fuels_properties", "01_hydrogen_ammonia_properties"
    if re.search(r"soot|polycyclic.aromatic|gas.soot", lower):
        return "05_diagnostics_radiation", "03_soot_formation"
    if re.search(r"reacting.flow|reactive.flow|reconstruct", lower):
        return "03_operators_reconstruction", "02_general_flow_reconstruction"
    return "10_reviews_methods", "02_crosscutting_methods"


def main():
    items = {}
    occurrences = collections.Counter()
    searches = []
    for path in sorted((ROOT / "evidence/discovery").glob("*.json")):
        if not path.name.startswith(("crossref_", "key_")):
            continue
        result = json.loads(path.read_text(encoding="utf-8"))
        searches.append({key: result.get(key) for key in ["query", "issn", "url", "retrieved_at", "total_results"]})
        for item in result["items"]:
            doi = item["DOI"].lower()
            occurrences[doi] += 1
            if doi not in items or (item.get("abstract") and not items[doi].get("abstract")):
                items[doi] = item
    included = []
    exclusions = []
    curated = json.loads((ROOT / "literature/curation.json").read_text(encoding="utf-8"))
    for doi, item in sorted(items.items()):
        title = re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", "", item.get("title", [""])[0]))).strip()
        journal = html.unescape(item.get("container-title", [""])[0])
        year = item.get("published", {}).get("date-parts", [[0]])[0][0]
        if re.search(r"fuel.cell|proton.exchange.membrane|post.combustion.*capture|post.combustion.carbon|heat.transformer|transformer.oil|hydrogen.*production|fuel.production|wind.driven.green|lipid.production|electricity,.cooling,.and.desalinated|iron.from.copper.slag|thermoacoustic.core|hydrodenitrogenation|hydrodesulfurization|\bhydrocrack", title, re.I):
            reason = "adjacent_energy_topic_outside_combustion_ai_scope"
        elif journal.lower() not in JOURNALS:
            reason = "journal_outside_current_screening_list"
        elif not AI.search(title) and doi not in curated:
            reason = "no_explicit_ai_method_in_title"
        elif journal.lower() not in CORE and not COMBUSTION.search(title) and doi not in curated:
            reason = "combustion_relevance_not_clear_from_title"
        elif re.search(r"editorial|copyright|contents|correction|corrigendum|retract|special.issue|erratum", title, re.I):
            reason = "non_research_or_correction_item"
        elif not 2018 <= year <= 2026:
            reason = "outside_date_window"
        else:
            category, subcategory = classify(title)
            included.append({"doi": doi, "title": title, "journal": journal, "year": year, "category": category, "subcategory": subcategory, "metadata": item, "screening": "title_review_pending", "jcr_status": "pending", "code_status": "not_yet_searched_per_paper", "duplicate_hits": occurrences[doi]})
            continue
        exclusions.append({"doi": doi, "title": title, "journal": journal, "reason": reason})
    included.sort(key=lambda item: (-item["year"], item["category"], item["doi"]))
    output = ROOT / "literature"
    output.mkdir(exist_ok=True)
    (output / "screened_candidates.json").write_text(json.dumps(included, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "evidence/screening.json").write_text(json.dumps({"date": "2026-11-11", "retrieved_hits": sum(occurrences.values()), "unique_records": len(items), "candidate_count": len(included), "searches": searches, "exclusions": exclusions}, ensure_ascii=False, indent=2), encoding="utf-8")
    for position, item in enumerate(included):
        print(f'{position:03d} | {item["year"]} | {item["doi"]} | {item["journal"]} | {item["title"]}')
    print("TOTAL", len(included), "JOURNALS", collections.Counter(item["journal"] for item in included))


if __name__ == "__main__":
    main()
