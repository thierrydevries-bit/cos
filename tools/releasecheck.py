#!/usr/bin/env python3
"""Releasecheck: harde controle voor elke release.

Gebruik:
  python3 tools/releasecheck.py            controleert de hele repo
  python3 tools/releasecheck.py --skill X  controleert een losse skillmap (bijv. de eigen versie)

Een vondst geeft exitcode 1 en stopt de release.
"""
import argparse
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("Installeer eerst PyYAML: pip install pyyaml")

MAX_BESCHRIJVING = 1024
MAX_NAAM = 64
NAAM = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VERBODEN_NAAM = ("anthropic", "claude")
STREEPJES = "—–"

fouten = []


def fout(pad, tekst):
    fouten.append(f"{pad}: {tekst}")


def voorwerk(pad):
    """Lees de YAML-kop. Geeft een dict, of None bij een fout."""
    tekst = pad.read_text(encoding="utf8")
    if not tekst.startswith("---\n"):
        fout(pad, "geen YAML-kop")
        return None
    delen = tekst.split("---\n", 2)
    if len(delen) < 3:
        fout(pad, "YAML-kop is niet afgesloten")
        return None
    try:
        kop = yaml.safe_load(delen[1])
    except yaml.YAMLError as e:
        fout(pad, f"YAML-kop klopt niet: {e}")
        return None
    if not isinstance(kop, dict):
        fout(pad, "YAML-kop is leeg")
        return None
    return kop


def check_skill(map_):
    pad = map_ / "SKILL.md"
    if not pad.exists():
        fout(map_, "SKILL.md ontbreekt")
        return
    kop = voorwerk(pad)
    if kop is None:
        return
    naam = kop.get("name")
    beschrijving = kop.get("description")
    if not naam:
        fout(pad, "name ontbreekt")
    else:
        if not NAAM.match(str(naam)):
            fout(pad, f"name '{naam}' mag alleen kleine letters, cijfers en streepjes hebben")
        if len(str(naam)) > MAX_NAAM:
            fout(pad, f"name is langer dan {MAX_NAAM} tekens")
        if any(w in str(naam) for w in VERBODEN_NAAM):
            fout(pad, f"name '{naam}' bevat een verboden woord")
        if str(naam) != map_.name:
            fout(pad, f"name '{naam}' wijkt af van de map '{map_.name}'")
    if not beschrijving or not str(beschrijving).strip():
        fout(pad, "description ontbreekt")
    else:
        lengte = len(str(beschrijving))
        if lengte > MAX_BESCHRIJVING:
            fout(pad, f"description is {lengte} tekens, de grens is {MAX_BESCHRIJVING}")
        if "<" in str(beschrijving) or ">" in str(beschrijving):
            fout(pad, "description bevat een punthaak")
    check_verwijzingen(map_)


def check_verwijzingen(map_):
    """Elke verwijzing naar een references-bestand moet bestaan, en elk bestand moet gebruikt worden."""
    ref = map_ / "references"
    bestanden = list(map_.rglob("*.md"))
    teksten = {p: p.read_text(encoding="utf8") for p in bestanden}
    if ref.is_dir():
        bestaand = {p.name for p in ref.glob("*.md")}
        for p, t in teksten.items():
            for m in re.findall(r"`references/([\w-]+\.md)`", t):
                if m not in bestaand:
                    fout(p, f"verwijst naar references/{m}, dat bestaat niet")
            for m in re.findall(r"`([\w-]+\.md)`", t):
                if m not in bestaand and m not in {"SKILL.md", "CHANGELOG.md", "README.md"}:
                    fout(p, f"verwijst naar {m}, dat bestaat niet")
        for naam in sorted(bestaand):
            if not any(naam in t for p, t in teksten.items() if p.name != naam):
                fout(ref / naam, "wordt nergens genoemd")
    for p, t in teksten.items():
        for teken in STREEPJES:
            if teken in t:
                fout(p, "bevat een gedachtestreepje")
                break


def check_commando(pad, skills):
    kop = voorwerk(pad)
    if kop is None:
        return
    if not kop.get("description"):
        fout(pad, "description ontbreekt")
    tekst = pad.read_text(encoding="utf8")
    for m in re.findall(r"`references/([\w-]+\.md)`", tekst):
        if not any((s / "references" / m).exists() for s in skills):
            fout(pad, f"verwijst naar references/{m}, dat bestaat niet")
    for m in re.findall(r"`(?:skills/[\w-]+/)?([\w-]+\.md)`", tekst):
        if m != "SKILL.md" and not any((s / "references" / m).exists() for s in skills):
            fout(pad, f"verwijst naar {m}, dat bestaat niet")


def check_repo(wortel):
    markt = wortel / ".claude-plugin" / "marketplace.json"
    try:
        marktdata = json.loads(markt.read_text(encoding="utf8"))
    except (OSError, ValueError) as e:
        fout(markt, f"niet leesbaar: {e}")
        return
    changelog = (wortel / "CHANGELOG.md").read_text(encoding="utf8")
    kop_log = next((r for r in changelog.splitlines() if r.startswith("## ")), "")
    if not kop_log:
        fout(wortel / "CHANGELOG.md", "geen versiekop")
    plugins = sorted(p for p in (wortel / "plugins").iterdir() if p.is_dir())
    namen = {p.get("name") for p in marktdata.get("plugins", [])}
    for plug in plugins:
        manifest = plug / ".claude-plugin" / "plugin.json"
        try:
            data = json.loads(manifest.read_text(encoding="utf8"))
        except (OSError, ValueError) as e:
            fout(manifest, f"niet leesbaar: {e}")
            continue
        versie = data.get("version", "")
        if not re.match(r"^\d+\.\d+\.\d+$", versie):
            fout(manifest, f"versie '{versie}' klopt niet")
        if data.get("name") != plug.name:
            fout(manifest, f"name '{data.get('name')}' wijkt af van de map")
        if plug.name not in namen:
            fout(markt, f"plug-in {plug.name} staat niet in de marketplace")
        if f" {versie}" not in changelog:
            fout(wortel / "CHANGELOG.md", f"versie {versie} van {plug.name} staat er niet in")
        skills = sorted(s for s in (plug / "skills").iterdir() if s.is_dir())
        for s in skills:
            check_skill(s)
            tekst = (s / "SKILL.md").read_text(encoding="utf8") if (s / "SKILL.md").exists() else ""
            m = re.search(r"Versie (\d+\.\d+(?:\.\d+)?),", tekst)
            if m and not versie.startswith(m.group(1)):
                fout(s / "SKILL.md", f"Versie {m.group(1)} wijkt af van plugin.json ({versie})")
        for c in sorted((plug / "commands").glob("*.md")) if (plug / "commands").is_dir() else []:
            check_commando(c, skills)
    eerste = next((p for p in plugins if p.name == "chief-of-staff-and-stuff"), None)
    if eerste and kop_log:
        v = json.loads((eerste / ".claude-plugin" / "plugin.json").read_text(encoding="utf8"))["version"]
        if v not in kop_log:
            fout(wortel / "CHANGELOG.md", f"bovenste kop noemt versie {v} niet: {kop_log}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", help="controleer alleen deze skillmap")
    a = ap.parse_args()
    if a.skill:
        check_skill(pathlib.Path(a.skill).resolve())
    else:
        check_repo(pathlib.Path(__file__).resolve().parent.parent)
    if fouten:
        print(f"RELEASE STOPT: {len(fouten)} vondst(en)")
        for r in fouten:
            print(f"- {r}")
        return 1
    print("SCHOON: releasecheck vond niets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
