---
tags:
  - router/screen
  - feature/decks
---
# Tela: DeckDetailsScreen

Visão aprofundada de um baralho específico, permitindo iniciar sessões de revisão, gerenciar cartões, editar propriedades ou excluir o baralho.

- **Arquivo no App**: [`lib/features/decks/screens/deck_details_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/screens/deck_details_screen.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📱 Estrutura e Recursos

1. **Cabeçalho e Ações**:
   - Título, descrição e menu contextual (Editar baralho, Excluir baralho com confirmação).
2. **Resumo de Status dos Cartões**:
   - Divisão visual dos cartões em:
     - **Novos** (`timesReviewed == 0`)
     - **Em Aprendizado** (`isInProgress`)
     - **Dominados** (`isMastered`)
3. **Botão Iniciar Sessão de Estudo**:
   - Habilitado se houver cartões pendentes de revisão (`card.isDue`).
   - Ao tocar, navega para a [[FlashcardSessionScreen]].
4. **Lista de Flashcards do Baralho**:
   - Listagem com pergunta e resposta resumidas.
   - Opção de toque para navegar para a [[EditFlashcardScreen]] ou excluir o cartão.
5. **Botão Adicionar Cartão**:
   - Navega para a [[CreateFlashcardScreen]].

---

## 🔗 Dependências

- Utiliza `deck_details_controller.dart` para filtros e estados locais.
- Acessa [[DeckService]] para disparar atualizações e remoções.
- Navega para:
  - [[FlashcardSessionScreen]]
  - [[CreateFlashcardScreen]]
  - [[EditFlashcardScreen]]
