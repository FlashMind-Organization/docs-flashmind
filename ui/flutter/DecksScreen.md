---
tags:
  - router/screen
  - feature/decks
---
# Tela: DecksScreen

Tela de gerenciamento e listagem geral de todos os baralhos de estudo cadastrados.

- **Arquivo no App**: [`lib/features/decks/screens/decks_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/screens/decks_screen.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📱 Estrutura Visual e Componentes

1. **`ScreenHeader`**:
   - Título "Meus Baralhos", subtítulo explicativo e botão de ajuda ("?") que abre o `DeckStatesHelpBottomSheet`.
2. **`DecksSummary`**:
   - Painel superior com estatísticas consolidadas: total de baralhos criados e soma geral de flashcards.
3. **`DeckList` & `DeckListItem`**:
   - Lista vertical de baralhos. Cada item exibe:
     - Título e descrição do baralho.
     - Contagem de cartões totais e cartões prontos para revisão hoje (`reviewedCards` vs `totalCards`).
     - Barra horizontal de progresso percentual.
     - Toque no item navega para a [[DeckDetailsScreen]].
4. **`CreateDeckButton`**:
   - Botão flutuante ou fixo para navegar até a [[CreateDeckScreen]].

---

## 🔗 Dependências

- Escuta o [[DeckService]] através de `ListenableBuilder` para reconstruir a lista automaticamente a cada criação, edição ou exclusão.
- Navega para:
  - [[DeckDetailsScreen]] (passando o baralho selecionado)
  - [[CreateDeckScreen]]
  - `DeckStatesHelpBottomSheet` (modal explicativo)
