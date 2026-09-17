#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de análise estática do app-flashmind e integridade do vault docs-flashmind.

Inspirado nos scripts geradores do lumos-docs, este utilitário analisa as
classes, models, widgets e controllers do Flutter em app-flashmind/lib e valida
a consistência de todos os wikilinks [[...]] do vault Obsidian.
"""

import glob
import os
import re
import json

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
APP_ROOT = os.path.abspath(os.path.join(DOCS_ROOT, "..", "app-flashmind"))
LIB_DIR = os.path.join(APP_ROOT, "lib")


def analyze_flutter_app():
    print("=" * 60)
    print("🔍 Analisando código Dart do app-flashmind...")
    print("=" * 60)

    if not os.path.isdir(LIB_DIR):
        print(f"❌ Diretório lib não encontrado em: {LIB_DIR}")
        return None

    dart_files = glob.glob(f"{LIB_DIR}/**/*.dart", recursive=True)
    print(f"Total de arquivos Dart encontrados: {len(dart_files)}")

    class_pat = re.compile(r"class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+(\w+))?")
    enum_pat = re.compile(r"enum\s+(\w+)")

    classes = {}
    enums = {}
    screens = []
    widgets = []
    services = []
    models = []

    for path in dart_files:
        rel_path = os.path.relpath(path, APP_ROOT)
        content = open(path, encoding="utf-8", errors="ignore").read()

        for match in class_pat.finditer(content):
            cname = match.group(1)
            ext = match.group(2)
            classes[cname] = {
                "file": rel_path,
                "extends": ext,
            }

            if cname.endswith("Screen"):
                screens.append((cname, rel_path))
            elif ext in ("StatelessWidget", "StatefulWidget", "Widget"):
                widgets.append((cname, rel_path))
            elif cname.endswith("Service") or cname.endswith("Controller"):
                services.append((cname, rel_path))
            elif "/models/" in rel_path:
                models.append((cname, rel_path))

        for match in enum_pat.finditer(content):
            ename = match.group(1)
            enums[ename] = rel_path

    print(f"\n📊 Métricas Extraídas:")
    print(f"  • Total de Classes Dart: {len(classes)}")
    print(f"  • Telas (Screens): {len(screens)}")
    print(f"  • Widgets Detectados: {len(widgets)}")
    print(f"  • Services/Controllers: {len(services)}")
    print(f"  • Modelos Identificados: {len(models)}")
    print(f"  • Enums Identificados: {len(enums)}")

    # Salva dados extraídos em _dados/app_meta.json
    out_dir = os.path.join(HERE, "_dados")
    os.makedirs(out_dir, exist_ok=True)
    meta_path = os.path.join(out_dir, "app_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "total_files": len(dart_files),
                "total_classes": len(classes),
                "screens": screens,
                "widgets": widgets,
                "services": services,
                "models": models,
                "enums": list(enums.keys()),
            },
            f,
            indent=2,
            ensure_ascii=False,
        )
    print(f"\n💾 Metadados gravados com sucesso em: {os.path.relpath(meta_path, DOCS_ROOT)}")
    return True


def verify_vault_links():
    print("\n" + "=" * 60)
    print("🔗 Verificando integridade de wikilinks [[...]] do vault...")
    print("=" * 60)

    md_files = glob.glob(f"{DOCS_ROOT}/**/*.md", recursive=True)
    notes = {os.path.splitext(os.path.basename(f))[0] for f in md_files}

    link_pat = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
    broken = []
    total_links = 0

    for md_file in md_files:
        rel_src = os.path.relpath(md_file, DOCS_ROOT)
        content = open(md_file, encoding="utf-8", errors="ignore").read()

        # Remove blocos de código cercados e inline para não pegar exemplos de código
        clean_content = re.sub(r"```[\s\S]*?```", "", content)
        clean_content = re.sub(r"`[^`\n]+`", "", clean_content)

        for m in link_pat.finditer(clean_content):
            total_links += 1
            target = m.group(1).strip()
            if target and target not in notes:
                broken.append((rel_src, target))

    print(f"Total de notas Markdown: {len(md_files)}")
    print(f"Total de wikilinks analisados: {total_links}")

    if not broken:
        print("✅ SUCESSO: Todos os links do vault estão 100% íntegros!")
    else:
        print(f"⚠️ ATENÇÃO: Encontrados {len(broken)} links sem destino correspondente:")
        for src, tgt in broken:
            print(f"  • {src} -> [[{tgt}]]")


if __name__ == "__main__":
    analyze_flutter_app()
    verify_vault_links()
