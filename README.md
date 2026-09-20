# FlashMind — Documentação Viva (Obsidian Vault)

O **docs-flashmind** é o cofre (*vault*) de documentação viva e análise de impacto do ecossistema FlashMind, estruturado para leitura, navegação bidirecional e exploração em grafo via [Obsidian](https://obsidian.md/).

Ele mantém contratos de domínio, especificações detalhadas de cada tela e componente móvel, regras invioláveis de negócio e planos de evolução arquitetural.

---

## 📋 Pré-requisitos

- **Leitura e Edição**: [Obsidian](https://obsidian.md/) (versão desktop para Linux/macOS/Windows ou mobile).
- **Validação de Código e Links**: Python `>= 3.10` (biblioteca padrão, sem dependências externas).

---

## 📖 Como Abrir e Navegar no Obsidian

1. Abra o aplicativo **Obsidian**.
2. Na tela inicial (ou no menu de cofres), clique em **"Open folder as vault"** (*Abrir pasta como cofre*).
3. Selecione o diretório desta pasta:
   ```text
   /home/jonas/Projects/flashmind/docs-flashmind
   ```
4. Utilize a nota **`_indice.md`** ou abra a visualização em grafo (**Ctrl + G** ou **Graph View**) para explorar as conexões conceituais entre modelos, telas e serviços.

---

## 🔍 Scanner Automático e Validador de Links

O cofre inclui um utilitário de validação e extração estática em Python (`_gerador/scan_app.py`).

Ele executa:
1. **Varredura no app Flutter (`app-flashmind/lib/`)**: Identifica classes, telas (*screens*), widgets, services/controllers, modelos e enums, atualizando o arquivo de metadados em `_gerador/_dados/app_meta.json`.
2. **Validação de Wikilinks (`[[...]]`)**: Analisa todas as notas markdown do cofre e garante que nenhum link esteja quebrado.

### Como executar:

```bash
cd docs-flashmind
python3 _gerador/scan_app.py
```

Exemplo de saída de sucesso:
```text
============================================================
🔍 Analisando código Dart do app-flashmind...
============================================================
Total de arquivos Dart encontrados: 82

📊 Métricas Extraídas:
  • Total de Classes Dart: 95
  • Telas (Screens): 12
  • Widgets Detectados: 32
  • Services/Controllers: 11
  • Modelos Identificados: 9
  • Enums Identificados: 2

💾 Metadados gravados com sucesso em: _gerador/_dados/app_meta.json

============================================================
🔗 Verificando integridade de wikilinks [[...]] do vault...
============================================================
Total de notas Markdown: 45
Total de wikilinks analisados: 226
✅ SUCESSO: Todos os links do vault estão 100% íntegros!
```

---

## 📂 Estrutura do Vault

```text
docs-flashmind/
├── _gerador/                  # Scripts utilitários de análise e dados extraídos
│   ├── scan_app.py            # Validador de integridade e scanner do app Flutter
│   └── _dados/app_meta.json   # Metadados extraídos das entidades Flutter
├── dominios/                  # Regras de negócio essenciais
│   ├── Gamificação e Progresso.md
│   ├── Repetição Espaçada.md
│   └── Contas e Baralhos.md
├── ui/flutter/                # Documentação técnica das telas e widgets do Flutter
│   ├── HomeScreen.md
│   ├── AuthGate.md
│   ├── LoginScreen.md
│   ├── RegisterScreen.md
│   ├── ProfileScreen.md
│   └── AdminDashboardScreen.md
├── models/flutter/            # Especificação de entidades de dados
│   ├── Deck.md
│   ├── Flashcard.md
│   ├── UserProgress.md
│   └── AuthUser.md
├── clientes/flutter/          # Injeção de dependência e serviços
│   ├── AppScope.md
│   ├── DeckService.md
│   └── AuthService.md
└── guias/                     # Diretrizes e evolução
    └── Plano de Transição para a API.md
```
