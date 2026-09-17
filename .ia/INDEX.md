# IA do FlashMind Docs (docs-flashmind)

Contexto específico para manutenção do vault Obsidian de documentação viva e análise de impacto do FlashMind.

| Para entender | Leia |
|---|---|
| **Índice geral do vault** | `../Home.md` |
| **Convenções de tags** | `../Home.md#convenções-de-tag` |
| **Como manter e regenerar notas** | `../guias/Como manter este vault.md` |
| **Automação do scan estático** | `../_gerador/README.md` |

## Regras do Repositório

1. **Integridade de Links**: Todos os `[[wikilinks]]` devem apontar para notas existentes no vault.
2. **Tags Padronizadas**: Utilize as tags `#dominio`, `#guia`, `#model/flutter`, `#router/screen`, `#service/flutter`, etc.
3. **Validação**: Execute `python3 _gerador/scan_app.py` antes de concluir qualquer tarefa de documentação.
