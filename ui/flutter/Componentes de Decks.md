---
tags:
  - component/flutter
  - feature/decks
---
# Componentes: Decks

Conjunto de widgets modulares utilizados nas telas de baralhos e detalhes.

- **Diretório no App**: [`lib/features/decks/widgets/`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/widgets/)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 🧩 Catálogo de Componentes

### 1. `DeckList` (`deck_list.dart`)
- **Papel**: Renderiza a lista rolável com separadores e suporte a estado vazio amigável quando nenhum baralho foi encontrado na busca ou criado.
- **Filho**: `DeckListItem`.

### 2. `DeckListItem` (`deck_list_item.dart`)
- **Papel**: Cartão individual que exibe:
  - Título em negrito e descrição resumida.
  - Indicador numérico de cartões prontos para revisão vs total.
  - Barra de progresso percentual customizada.
  - Efeito visual de clique (*InkWell/Card*).

### 3. `DecksSummary` (`decks_summary.dart`)
- **Papel**: Painel horizontal superior na [[DecksScreen]], consolidando:
  - Total de baralhos ativos.
  - Total de flashcards acumulados no app.

### 4. `CreateDeckButton` (`create_deck_button.dart`)
- **Papel**: Botão estilizado de ação rápida que direciona para a [[CreateDeckScreen]].

### 5. `ScreenHeader` (`screen_header.dart`)
- **Papel**: Título principal, subtítulo descritivo e botão de interrogação que dispara o `DeckStatesHelpBottomSheet`.

### 6. `DeckStatesHelpBottomSheet` (`deck_states_help_bottom_sheet.dart`)
- **Papel**: Modal explicativo aberto a partir do header para esclarecer os 3 estados dos cartões:
  - *Novos*: nunca revisados.
  - *Em Aprendizado*: em revisão ativa.
  - *Dominados*: alcançaram intervalo longo de fixação.
