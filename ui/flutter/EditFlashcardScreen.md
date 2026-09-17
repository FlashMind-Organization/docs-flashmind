---
tags:
  - router/screen
  - feature/flashcards
---
# Tela: EditFlashcardScreen

Permite editar a pergunta, a resposta ou excluir um flashcard existente.

- **Arquivo no App**: [`lib/features/flashcards/screens/edit_flashcard_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/screens/edit_flashcard_screen.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📱 Estrutura e Ações

1. **Edição de Pergunta e Resposta**:
   - Campos pré-populados com os dados atuais do cartão.
2. **Validações**:
   - Campos obrigatórios e validação de duplicidade com outros cartões do baralho (excluindo o próprio ID do cartão).
3. **Ações**:
   - **Salvar Alterações**: aciona `DeckService.updateFlashcard(...)`.
   - **Excluir Cartão**: botão de perigo com diálogo de confirmação, acionando `DeckService.deleteFlashcard(...)`.

---

## 🔗 Dependências

- `EditFlashcardController`
- [[DeckService]]
- Entidades: [[Deck]], [[Flashcard]]
