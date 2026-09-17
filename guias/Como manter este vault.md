---
tags:
  - guia
  - manutencao
---
# Guia: Como Manter Este Vault

Este documento orienta desenvolvedores e agentes sobre como navegar, atualizar e expandir a documentação viva do **FlashMind**.

---

## 🗂️ O que é Manual e o que é Derivado

| Diretório / Arquivo | Natureza | Diretriz de Edição |
|---|---|---|
| `Home.md` | Manual | Atualizar quando novas features, telas ou marcos forem atingidos |
| `dominios/*.md` | Curadoria manual | Documentação de regras de negócio de alto nível |
| `guias/*.md` | Curadoria manual | Procedimentos arquiteturais e especificações |
| `models/flutter/*.md` | Mapeamento de código | Manter sincronizado com os modelos em `app-flashmind/lib/**/models/` |
| `clientes/flutter/*.md` | Mapeamento de código | Manter sincronizado com serviços e repositórios |
| `ui/flutter/*.md` | Mapeamento de UI | Documentar props, estados e dependências de cada tela |
| `_gerador/` | Scripts de automação | Scripts Python para inspeção de AST e validação de links |

---

## 🔍 Verificação de Links Quebrados (Sanity Check)

Para garantir que nenhum `[[wikilink]]` aponte para um arquivo inexistente no Obsidian:

```bash
cd /home/jonas/Projects/flashmind/docs-flashmind
python3 -c "
import glob, os, re
notes = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob('**/*.md', recursive=True)}
bad = []
for f in glob.glob('**/*.md', recursive=True):
    content = open(f, encoding='utf-8').read()
    for m in re.findall(r'\[\[([^\]|#]+)', content):
        target = m.strip()
        if target and target not in notes:
            bad.append((f, target))

if not bad:
    print('✅ Todos os wikilinks estão íntegros!')
else:
    print(f'❌ Encontrados {len(bad)} links quebrados:')
    for src, tgt in bad:
        print(f'  {src} -> [[{tgt}]]')
"
```

---

## 🔄 Quando a API for Iniciada

Quando o diretório `/home/jonas/Projects/flashmind/api-flashmind` for implementado:
1. Adicione a pasta `api/rotas/`, `api/modulos/` e `api/schemas/` no vault.
2. Ative os scripts em `_gerador/` para extrair automaticamente o `app.openapi()` do FastAPI e mapear para as datasources do Flutter, espelhando a automação completa do `lumos-docs`.
