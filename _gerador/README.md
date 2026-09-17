# Gerador e Analisador do Vault FlashMind

Este diretório contém os scripts de análise estática e automação do **`docs-flashmind`**, inspirados no pipeline do **`lumos-docs`**.

---

## 🚀 Como Executar

Para analisar o código do `app-flashmind`, extrair classes/métricas e verificar a integridade dos links do vault:

```bash
python3 _gerador/scan_app.py
```

O script:
1. Varre `app-flashmind/lib/` em busca de classes, telas, widgets, modelos, enums e serviços.
2. Salva os metadados em `_gerador/_dados/app_meta.json`.
3. Valida se todos os `[[wikilinks]]` das notas Markdown possuem correspondentes válidos.

---

## 🔮 Expansão Futura (com `api-flashmind`)

Quando a API em FastAPI for iniciada, adicionaremos os scripts:
- `spec.py`: executa `app.openapi()` da API e gera os contratos de rotas em `api/rotas/`.
- `models.py`: analisa a AST de `app/models/` para documentar tabelas e colunas.
- `trace.py`: conecta rotas às chamadas HTTP do app mobile.
