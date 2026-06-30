#!/usr/bin/env python3
"""Search the Custo Brasil corpus by filters.

Usage:
    python search_corpus.py [--category CAT] [--year YEAR] [--keyword KEYWORD]
                            [--state UF] [--type TYPE] [--source FAMILY]
                            [--recent N] [--json] [--check-changelog]

Examples:
    python search_corpus.py --category nota_tecnica --year 2023
    python search_corpus.py --keyword "split payment"
    python search_corpus.py --state SP
    python search_corpus.py --recent 10 --json
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path


def load_front_matter(path: Path) -> dict:
    """Parse YAML-like front matter (between --- markers)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def iter_documents(corpus_root: Path):
    """Yield (path, front_matter) pairs for all documented files."""
    if not corpus_root.is_dir():
        return
    for fname in ("document.md", "README.md"):
        for path in sorted(corpus_root.rglob(fname)):
            fm = load_front_matter(path)
            if fm.get("slug"):
                yield path, fm


def slug_to_path(corpus_root: Path, slug: str) -> Path | None:
    """Find a document directory by slug."""
    for fname in ("document.md", "README.md"):
        for path in corpus_root.rglob(fname):
            fm = load_front_matter(path)
            if fm.get("slug") == slug:
                return path.parent
    return None


def search(
    corpus_root: Path,
    *,
    category: str | None = None,
    year: str | None = None,
    keyword: str | None = None,
    state: str | None = None,
    doc_type: str | None = None,
    source_family: str | None = None,
    recent: int | None = None,
    changelog_root: Path | None = None,
    slug: str | None = None,
) -> list[dict]:
    results = []

    for path, fm in iter_documents(corpus_root):
        slug_val = fm.get("slug", "")

        if slug and slug_val != slug:
            continue

        if category and fm.get("category") != category:
            continue

        if source_family and fm.get("source_family") != source_family:
            continue

        if state:
            if f"Estado de {state}" not in str(path.parent):
                continue

        if doc_type:
            if doc_type == "nt" and not slug_val.startswith("nt-"):
                continue
            if doc_type == "it" and not slug_val.startswith("it"):
                continue
            if doc_type == "tabela" and not slug_val.startswith("tabela-"):
                continue
            if doc_type == "cbenef" and not slug_val.startswith("cbenef-"):
                continue
            if doc_type == "manual" and not slug_val.startswith("manual-") and not slug_val.startswith("moc-"):
                continue

        if year:
            year_match = re.search(r"(?:^|-)(\d{4})", slug_val)
            if not year_match or year_match.group(1) != year:
                continue

        title = fm.get("title", "") or path.parent.name

        if keyword:
            kw_lower = keyword.lower()
            if kw_lower not in slug_val.lower() and kw_lower not in title.lower():
                continue

        converted = fm.get("converted_at_utc", "")
        rel_path = path.parent.relative_to(corpus_root).as_posix()

        entry = {
            "slug": slug_val,
            "title": title,
            "category": fm.get("category", ""),
            "path": f"corpus/{rel_path}",
            "converted_at": converted,
            "source_family": fm.get("source_family", ""),
            "status": fm.get("status", ""),
            "original_sha256": fm.get("original_sha256", ""),
        }

        if changelog_root and slug_val:
            cl_path = None
            for p in changelog_root.rglob(f"{slug_val}.md"):
                cl_path = p
                break
            if cl_path:
                cl_text = cl_path.read_text(encoding="utf-8")
                ver_m = re.search(r"##\s+v?(\d[\d.]+\d)", cl_text)
                if ver_m:
                    entry["changelog_version"] = ver_m.group(1)
                date_m = re.search(r"- (\d{4}-\d{2}-\d{2}T\d{2}:\d{2})", cl_text)
                if date_m:
                    entry["changelog_last_update"] = date_m.group(1)

        results.append(entry)

    if recent:
        def _sort_key(e):
            ts = e.get("converted_at") or e.get("changelog_last_update") or ""
            return ts
        results.sort(key=_sort_key, reverse=True)
        results = results[:recent]

    return results


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Search corpus documents")
    parser.add_argument("--corpus-root", default="corpus")
    parser.add_argument("--changelog-root", default="changelog")
    parser.add_argument("--category")
    parser.add_argument("--year")
    parser.add_argument("--keyword")
    parser.add_argument("--state")
    parser.add_argument("--type", dest="doc_type",
                        choices=["nt", "it", "tabela", "cbenef", "manual"])
    parser.add_argument("--source")
    parser.add_argument("--slug")
    parser.add_argument("--recent", type=int)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--check-changelog", action="store_true")

    args = parser.parse_args()

    root = Path(args.corpus_root).resolve()
    cl_root = Path(args.changelog_root).resolve() if args.check_changelog else None

    results = search(
        root,
        category=args.category,
        year=args.year,
        keyword=args.keyword,
        state=args.state,
        doc_type=args.doc_type,
        source_family=args.source,
        recent=args.recent,
        changelog_root=cl_root,
        slug=args.slug,
    )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("Nenhum documento encontrado.")
            return 0
        print(f"Encontrados {len(results)} documento(s):\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['slug']}")
            print(f"   ├─ título: {r['title'][:80]}")
            print(f"   ├─ categoria: {r['category']}")
            print(f"   ├─ path: {r['path']}")
            if r.get("converted_at"):
                print(f"   ├─ convertido: {r['converted_at']}")
            if r.get("changelog_version"):
                print(f"   ├─ versão: {r['changelog_version']}")
            if r.get("changelog_last_update"):
                print(f"   └─ último update: {r['changelog_last_update']}")
            else:
                print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
